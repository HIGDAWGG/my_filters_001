import os, sys, json, datetime, socket, random, publicsuffixlist

dead_domains = []
p = publicsuffixlist.PublicSuffixList()

def get_whois_data_raw(domain, server):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((server, 43))
	all_data = b""
	s.send("{domain}\r\n".replace("{domain}", domain).encode())
	while True:
		try:
			newdata = s.recv(100)
			if len(newdata) == 0:
				break
			all_data += newdata
		except Exception:
			break
	s.close()
	return all_data.decode()

def get_whois(domain):
	tld = p.publicsuffix(domain).upper()
	server = f"{tld}.whois-servers.net"
	return get_whois_data_raw(domain, server)

def whois_exists(domain):
    try:
        whois_data = get_whois(domain)
        if "No match for" in whois_data or "No Data Found" in whois_data:
            return False
        return whois_data != ""
    except:
        return False

def is_alive(domain):
    global dead_domains
    try:
        return socket.gethostbyname(domain) != "0.0.0.0"
    except:
        if domain not in dead_domains and whois_exists(domain) == False:
            dead_domains.append(domain)
        return False

try:
    entry_data = json.loads(open("entry_data.json", encoding="UTF-8").read())
except:
    entry_data = {}

domain_list = open("Alternative list formats/antimalware_domains.txt", encoding="UTF-8").read().replace("\r\n","\n").split("\n")
current_date = datetime.datetime.now().isoformat()
entry_data["last_updated"] = current_date


for e in domain_list:
    if e not in entry_data and e != "last_updated":
        entry_data[e] = {
            "first_seen": current_date,
            "last_seen": current_date,
            "removed": False,
            "removed_date": "",
            "last_checked": current_date,
            "check_counter": random.randint(0, 35),
            "check_status": is_alive(e),
            "ever_rechecked": False,
            "readded": False,
            "origin_add": "",
            "readd": ""
        }
    else:
        if "check_status" not in entry_data[e]:
            domain_is_alive = is_alive(e)
            entry_data[e]["check_status"] = domain_is_alive
            entry_data[e]["last_checked"] = current_date
            entry_data[e]["check_counter"] = 0
            entry_data[e]["ever_rechecked"] = True
        if entry_data[e]["check_status"] == False:
            dead_domains.append(e)
        if "removed" in entry_data[e]:
            if entry_data[e]["removed"] == True:
                entry_data[e]["readded"] = True
                entry_data[e]["readd"] = current_date
                entry_data[e]["origin_add"] = entry_data[e]["first_seen"]
        entry_data[e]["last_seen"] = current_date
        entry_data[e]["removed"] = False
        entry_data[e]["removed_date"] = ""
        if "check_counter" not in entry_data[e]:
            entry_data[e]["check_counter"] = random.randint(0, 45)
        if "last_checked" not in entry_data[e]:
            entry_data[e]["last_checked"] = "Unknown"
        entry_data[e]["check_counter"] += 1
        if entry_data[e]["check_counter"] > 50:
            domain_is_alive = is_alive(e)
            entry_data[e]["check_status"] = domain_is_alive
            entry_data[e]["last_checked"] = current_date
            entry_data[e]["check_counter"] = 0
            entry_data[e]["ever_rechecked"] = True

for e in entry_data:
    if e not in domain_list and e != "last_updated":
        try:
            entry_data[e]["removed"] = True
            entry_data[e]["removed_date"] = current_date
        except Exception as err:
            print(err, e, entry_data[e])

entry_data_file = open("entry_data.json", 'w', encoding="UTF-8")
entry_data_file.write(json.dumps(entry_data))
entry_data_file.close()

dead_stuff = open("dead.mwbcheck.txt", 'w', encoding='UTF-8')
dead_stuff.write("\n".join(dead_domains))
dead_stuff.close()
