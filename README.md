# My filters
This is a collection of filterlists made by me (iam-py-test).<br>
Feel free to use any and all of them (they are under CC0) in [uBlock Origin](https://github.com/gorhill/uBlock), AdGuard, AdBlock Plus (special version required), or in any other way (i.e. PiHole, /etc/hosts) <br/>
Please report any issues you have and I will try to fix them; please note I may not reply within the day the issue is posted as I am often busy.<br>
Thank you to all the people in https://github.com/iam-py-test/my_filters_001/blob/main/CONTRIBUTORS.md for helping improve these filters.<br>
For uBlock Origin users, you can right click on any link starting with `https://subscribe.adblockplus.org`, click "uBlock Origin", then "Subscribe to filterlist...":<br>
<img src="https://raw.githubusercontent.com/iam-py-test/my_filters_001/main/wiki/right%20click%20to%20add.jpg" alt="The Firefox context menu when clicking on a filterlist subscribe link, showing the uBlock Origin options" title="This shows the Firefox context menu, but it should work in any browser supporting the latest version of uBo. uBo lite is not supported (yet) and may will never be"><br>

**The malicious website blocklist should now work in AdGuard on Windows. Please try it out (especially in AdGuard on Mac, iOS, and Android as I lack the ability to test those versions) and report any bugs. [Make sure you are using the designated version](https://raw.githubusercontent.com/iam-py-test/my_filters_001/main/Alternative%20list%20formats/antimalware_adguard_app.txt)**

Please note! I am only one person, and I do not have much time to dedicate to this project. These lists _don't_ get updated as often as they should, and I'm sorry.

### Some stats: 
<a href="https://github.com/iam-py-test/my_filters_001/blob/main/stats.md"><img src="https://raw.githubusercontent.com/iam-py-test/my_filters_001/main/totalentries.svg" width='130' height="20"></a>
<img src="https://img.shields.io/github/last-commit/iam-py-test/my_filters_001"> 
[![Update the alt lists](https://github.com/iam-py-test/my_filters_001/actions/workflows/update_filterlists.yml/badge.svg)](https://github.com/iam-py-test/my_filters_001/actions/workflows/update_filterlists.yml)

## Filters in this repo

#### Actively maintained
- The malicious website blocklist (antimalware.txt) ([Subscribe](https://subscribe.adblockplus.org/?location=https://raw.githubusercontent.com/iam-py-test/my_filters_001/main/antimalware.txt&title=The%20malicious%20website%20blocklist))

#### Automatically generated
- DuckDuckGo Clean up (duckduckgo-clean-up.txt) - Generated from The malicious website blocklist and iam-py-test's anti-PUP list
- Brave Search Clean up (brave-clean-up.txt) - Generated from The malicious website blocklist and iam-py-test's anti-PUP list
- Everything in the _Alternative list formats_ folder
- [The Malicious Website Blocklist lite](https://raw.githubusercontent.com/iam-py-test/my_filters_001/main/Alternative%20list%20formats/antimalware_lite.txt)


#### Not actively maintained but don't require frequent updates
- [My anti-Facebook list](https://github.com/iam-py-test/my_filters_001/blob/main/special_lists/antifacebook.txt)
- Anti-Norton tracking list HOSTs file (anti-norton-tracking.txt)
- iam-py-test's Discord cleanup list ([discord_cleanup.txt](https://raw.githubusercontent.com/iam-py-test/my_filters_001/main/discord_cleanup.txt))
- DuckDuckGo Additional Cleanup ([duckduckgo_extra_clean.txt](https://raw.githubusercontent.com/iam-py-test/my_filters_001/main/duckduckgo_extra_clean.txt))
- Anti-Dynamic DNS ([antidynamicdns.txt](https://raw.githubusercontent.com/iam-py-test/my_filters_001/main/antidynamicdns.txt))
- [iam-py-test's anti-PUP list](https://raw.githubusercontent.com/iam-py-test/my_filters_001/main/antipup.txt)


#### Not frequently updated but still receive occasional updates
- Anti-typosquatting list (antitypo.txt)
- Anti-redirectors list (anti-redirectors.txt)
- Anti-'JavaScript is disabled' warnings (no-js-warnings.txt)


#### Extension lists which add onto my existing lists
- [The malicious website blocklist - uBlock Origin extension](https://github.com/iam-py-test/my_filters_001/blob/main/special_lists/anti-malware-ubo-extension.txt)

#### Updated rarely but still technically supported
- My anti-rickroll list (anti-rickroll-list.txt)
- The clickbait blocklist (clickbait.txt) ([Subscribe](https://subscribe.adblockplus.org/?location=https://raw.githubusercontent.com/iam-py-test/my_filters_001/main/clickbait.txt&title=Clickbait%20Blocklist))
- [My Enhanced Protection list](https://github.com/iam-py-test/my_filters_001/blob/main/enhanced_protection.txt) (Warning: This list is pretty much unmaintained and very poorly thought out)
- Annoyances (annoyances.txt)

#### Lists for testing syntax
- Everything in the _Sandbox_ folder
- The useless filter list (useless-list.txt)
- test_filter.txt

#### Lists which I gave up on
- Pornography Blocklist (porn.txt)
- The device privacy list (device_privacy.txt)
- Anti-cookie-consent and paywalls list (anti-cookie+sign up.txt)
- [Google Safe Browsing reverse-engineered](https://github.com/iam-py-test/my_filters_001/blob/main/special_lists/google-safe-browsing-reverse-engineered.txt)
- [Microsoft Smart Screen reverse-engineered](https://github.com/iam-py-test/my_filters_001/blob/main/special_lists/microsoft-smart-screen-reverse-engineered.txt)


#### Dead lists which are not even complete
- trojan_protection_list.txt
- Anti-over-promoted Windows antivirus list (could not find enough instances of this that would not break legitimate websites)
- anti-cookie+sign up_extention.txt (had one purpose - to work with my custom scriptlets - but the website it was intended to work for changed cookie values to quickly for it to work)

#### Personal (would not recommend using)
- "Personal filters" (iam-py-test.txt)
- "Lockdown mode"
This list has an extremely specific purpose, and **SHOULD NOT BE USED**.

#### Experimental lists (use with care)
- TLD blocking lists ([more information](https://github.com/iam-py-test/my_filters_001/tree/main/region_blocklist))
- Anti-'page visit counter' list (anti-visit.txt)
- IP Lookup service blocklist ([antiiplookup.txt](https://raw.githubusercontent.com/iam-py-test/my_filters_001/main/antiiplookup.txt))
- Anti-adfly (anti-adfly.txt)
- Link redirect removal list (redirect-remover.txt)

<br>The filters in the _Alternative list formats_ folder are versions of some of the lists above for different software. These are auto-generated, and thus updates to them must be made to the original list or [the Python script](https://github.com/iam-py-test/my_filters_001/blob/main/scripts/update.py) which generates them.<br>
Everything not listed above, like the filters in the _Personal_ folder, is either completely forgotten by me, or is likely to break websites due to its purpose or lack of regulation. <br>

## Other formats

#### The malicious website blocklist
- HOSTs format - https://raw.githubusercontent.com/iam-py-test/my_filters_001/main/Alternative%20list%20formats/antimalware_hosts.txt
- Domains only - https://raw.githubusercontent.com/iam-py-test/my_filters_001/main/Alternative%20list%20formats/antimalware_domains.txt
- IP Addresses only - https://raw.githubusercontent.com/iam-py-test/my_filters_001/main/Alternative%20list%20formats/antimalware_ips.txt
- AdGuard Windows/MacOS (beta) - https://raw.githubusercontent.com/iam-py-test/my_filters_001/main/Alternative%20list%20formats/antimalware_adguard_app.txt
- AdGuard Home (untested) - https://raw.githubusercontent.com/iam-py-test/my_filters_001/main/Alternative%20list%20formats/antimalware_adguard_home.txt
- dnsmasq (untested) - https://raw.githubusercontent.com/iam-py-test/my_filters_001/main/Alternative%20list%20formats/antimalware_dnsmasq.txt
- JSON - https://raw.githubusercontent.com/iam-py-test/my_filters_001/main/Alternative%20list%20formats/antimalware_json.json
- HOSTs format (no comments) - https://raw.githubusercontent.com/iam-py-test/my_filters_001/main/Alternative%20list%20formats/antimalware_pure_hosts.txt
- AdBlock Plus format (not recommended) - https://raw.githubusercontent.com/iam-py-test/my_filters_001/main/Alternative%20list%20formats/antimalware_abp.txt

#### Clickbait blocklist (unmaintained)
- AdBlock Plus format - https://raw.githubusercontent.com/iam-py-test/my_filters_001/main/Alternative%20list%20formats/clickbait_abp.txt
- Domains only - https://raw.githubusercontent.com/iam-py-test/my_filters_001/main/Alternative%20list%20formats/clickbait_domains.txt

#### Pornography Blocklist (unmaintained)
- HOSTs format - https://github.com/iam-py-test/my_filters_001/blob/main/Alternative%20list%20formats/porn_hosts.txt
- AdBlock Plus format - https://github.com/iam-py-test/my_filters_001/blob/main/Alternative%20list%20formats/porn_abp.txt
- Domains only (i.e., PiHole) - https://github.com/iam-py-test/my_filters_001/blob/main/Alternative%20list%20formats/porn_domains.txt
- Pure (no comments) HOSTs format - https://github.com/iam-py-test/my_filters_001/blob/main/Alternative%20list%20formats/porn_pure_hosts.txt

## Projects which use my lists (to my knowledge)
- [pallebone's PersonalPiholeListsPAllebone](https://github.com/pallebone/PersonalPiholeListsPAllebone) uses the domains version of the malicious website blocklist
- [eded333's TheF\*ckingList](https://github.com/eded333/TheFuckingList) uses the uBlock Origin version of the malicious website blocklist and the Anti-Norton Tracking list
- [hagezi's DNS Blocklists](https://github.com/hagezi/dns-blocklists) use the domains version of the malicious website blocklist
- [The oisd blocklist](https://oisd.nl) includes my antitypo list in their full list, and my Porn blocklist in their NSFW list
## Mentions
- [fynks's extension configuration](https://github.com/fynks/configs#extension-configs-)
- [yokoffing's recommended lists](https://github.com/yokoffing/filterlists#security)

These are not endorsements. 

#### Notes
- The DuckDuckGo Clean Up list is auto-generated from duckduckgo-clean-up.template and the domains/ips versions of The malicious website blocklist. Changes in Pull Requests should be made to The malicious website blocklist or to [the Python script](https://github.com/iam-py-test/my_filters_001/blob/main/scripts/update-duckduckgo-clean-up.py). 
- Like above, The Brave Search Clean Up list is auto-generated from brave-clean-up.template and the domains/ips versions of The malicious website blocklist. Changes in Pull Requests should be made to The malicious website blocklist or [the Python script](https://github.com/iam-py-test/my_filters_001/blob/main/scripts/update-brave-clean-up.py).
- Google Safe Browsing reverse engineered and Microsoft Smartscreen reverse engineered _are not_ intended as lists of known malware domains, instead they are lists of domains/urls which are blocked by those services in an attempt to understand them and provide some of their protection to users of other browsers. They are also rarely updated
- All the up-to-date HOSTs versions use 0.0.0.0 instead of 127.0.0.1, as per [#87](https://github.com/iam-py-test/my_filters_001/issues/87)
- The _domains_lite_ and _hosts_lite_ versions are unmaintained as they took too much time to create and the script(s) which made them have been lost to history, however, the antimalware_lite is not.
- _The malicious website blocklist - uBlock Origin extension_ should not be installed on its own as it is designed only to be included in _The malicious website blocklist_.
