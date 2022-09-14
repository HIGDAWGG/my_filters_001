import os,sys
import datetime
from publicsuffixlist import PublicSuffixList

psl = PublicSuffixList()

list1 = """[Adblock Plus 2.0]
! Title: The malicious website blocklist (lite)
! Description: I released that a lot of the domains in my antimalware list used the same TLDs, and those TLDs had almost no legit content. 
! Homepage: https://github.com/iam-py-test/my_filters_001
! Issues url: https://github.com/iam-py-test/my_filters_001/issues
! GitLab issues url (not checked as often): https://gitlab.com/iam-py-test/my_filters_001/-/issues
! Script last updated: 14/9/2022
! Last updated: {}
! Expires: 1 day

! Main blocking rules
||gdn^$document
||bid^$document
||loan^$documen

! Domain/url blocking rules (auto-generated)
""".format(datetime.datetime.now().strftime("%d/%m/%y %H:%M"))
blockedtlds = ["gdn","bid","loan"]

lines = open("antimalware.txt").read().split("\n")
for line in lines:
  if line.startswith("||"):
    list1 += line + "\n"
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
    except:
      list1 += line + "\n"
endlist = open("Alternative list formats/antimalware_lite.txt","w")
endlist.write(list1)
endlist.close()
