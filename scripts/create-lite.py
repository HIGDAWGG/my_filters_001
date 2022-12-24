import datetime
import requests
import publicsuffixlist

psl = publicsuffixlist.PublicSuffixList()

list1 = """[Adblock Plus 2.0]
! Title: The malicious website blocklist (lite)
! Description: A lighter version of The malicious website blocklist, which has no comments and has some extra protections against breakage
! Homepage: https://github.com/iam-py-test/my_filters_001
! Issues url: https://github.com/iam-py-test/my_filters_001/issues
! GitLab issues url (not checked as often): https://gitlab.com/iam-py-test/my_filters_001/-/issues
! Script last updated: 24/12/2022
! Last updated: {}
! Expires: 1 day

! Main blocking rules
||gdn^$document

! Domain/url blocking rules (auto-generated)
""".format(datetime.datetime.now().strftime("%d/%m/%y"))
blockedtlds = ["gdn"]
done_entries = []
bannedfilters = []
try:
  bannedfilters += list(filter(bool,requests.get("https://raw.githubusercontent.com/iam-py-test/allowlist/main/filter.txt").text.split("\n")))
except:
  pass


lines = open("antimalware.txt").read().split("\n")
for line in lines:
  if line in done_entries or line in bannedfilters:
    continue
  if line.startswith("||") and "/" in line:
    list1 += line + "\n"
    done_entries.append(line)
    continue
  if line.startswith("!") or line == "" or line.startswith("#") or "[Adblock Plus 2.0]" in line:
    continue
  else:
    try:
      tld = psl.publicsuffix(line.split("$")[0])
      if tld in blockedtlds:
        continue
      else:
        list1 += line + "\n"
        done_entries.append(line)
    except:
      list1 += line + "\n"
      done_entries.append(line)
endlist = open("Alternative list formats/antimalware_lite.txt","w")
endlist.write(list1)
endlist.close()
