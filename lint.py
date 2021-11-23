"""Verify the syntax of my antimalware list and verify there are no legit domains in it"""

# domains which are good & should never be blocked in this list
gooddomains = ["google.com","www.google.com","duckduckgo.com","www.duckduckgo.com","virustotal.com","safeweb.norton.com","mywot.com","www-amazon-com.customer.fastly.net","fastly.net","adguardteam.github.io","iam-py-test.github.io","example.com","r3.o.lencr.org","mozilla.org","www.mozilla.org","www.mozorg.moz.works","addons.mozilla.org","github.community"]
# domains which are used for hosting or contain User Generated Content, and should only have subdomains/specific urls listed
hosting = ["duckdns.org","appspot.com","blogspot.com","raw.githubusercontent.com","github.com","gitlab.com","github.io","storage.cloud.google.com","mediafire.com","archive.org"]
# social media and email
social = ["reddit.com","twitter.com","slack.com","meet.google.com","mail.google.com","gmail.com","chat.google.com","discord.gift","discord.com"]
# url shorteners which should only have specific urls blocked
urlshorteners = ["bit.ly","x.co","tinyurl.com","t.co","t.ly","sites.google.com","urldefense.proofpoint.com"]
# invalid syntax in uBlock Origin
invalidsyntax = ["$$","$docment","$alll","^all","$docs","$scripted","|||","$alls","$documentall","$allall","$all$all","$all.","$docments"]

# the main text
maintext = open("antimalware.txt").read()
lines = maintext.split("\n")
# a list of invalid lines/good domains found
invalidlines = []
# log
log = ""

for line in lines:
    if line.startswith("!"):
        continue
    try:
      domain = line.split("^$")[0][2:]
      if domain in gooddomains or domain in hosting or domain in urlshorteners or domain in social:
        invalidlines.append(line)
        print("False positive detected: WARNING")
      for syntax in invalidsyntax:
        if syntax in line:
          invalidlines.append(line)
    except:
      continue

with open("invalidlines.md","w") as f:
  f.write("## Lines detected by Lint")
  for line in invalidlines:
    f.write("\n{}<br>".format(line))
  f.close()
  
