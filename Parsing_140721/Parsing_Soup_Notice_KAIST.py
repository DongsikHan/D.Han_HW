import urllib

from bs4 import BeautifulSoup

htmltext = urllib.urlopen("http://www.kaist.ac.kr/_prog/adcal/?dvs_cd=1&site_dvs_cd=kr&menu_dvs_cd=03030101").read()

soup = BeautifulSoup(htmltext, from_encoding="utf-8")

dates = []
events = []

for tag in soup.select("ul > li > strong"):
	dates.append(tag.get_text())

for tag in soup.select("p.r_con"):
	events.append(tag.get_text())

for i in range(len(dates)):
	print dates[i].encode("utf-8") + ": " + events[i].encode("utf-8")

# for event in events: 
# 	print event.encode("utf-8")



