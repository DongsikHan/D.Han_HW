from flask import render_template, Flask, request
from apps import app
import urllib2
from bs4 import BeautifulSoup

@app.route('/', methods=['GET', 'POST'])
def index():

    return render_template("index.html")

@app.route('/crawl', methods=['GET', 'POST'])
def crawl():
    
    month = None

    if 1 > int(request.args['text_get']) or int(request.args['text_get']) > 12:
        return "Error: out of range (1 ~ 12)"
    else:
        month = request.args['text_get']

    htmltext = urllib2.urlopen("http://www.kaist.ac.kr/_prog/adcal/?dvs_cd=1&site_dvs_cd=kr&menu_dvs_cd=03030101").read()

    soup = BeautifulSoup(htmltext, from_encoding="utf-8")

    dates = []
    events = []

    for tag in soup.select("ul > li > strong"):
        dates.append(tag.get_text())

    for tag in soup.select("p.r_con"):
        events.append(tag.get_text())

    result = ""

    for i in range(len(dates)):
        if dates[i].split('.')[0] == month:
           result = result + dates[i].encode("utf-8") + ": " + events[i].encode("utf-8") + "<br>"

    return result       

