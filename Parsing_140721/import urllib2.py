import urllib2
 
def kaist_notice_list(pageNum):
	response = urllib2.urlopen('http://www.kaist.ac.kr/_prog/_board/?code=kaist_event&site_dvs_cd=kr&menu_dvs_cd=0602&skey=&sval=&site_dvs=&GotoPage=&GotoPage=%d'%(pageNum))
	html = response.read().split('<td class="title">')
	for a in range(len(html)-1): 
		data = html[a+1]
		print "    " + str(a+1) + ". " +data.split('</a>')[0].split("=%d'>"%(pageNum))[1]
 
for i in range(1,5):
	print "\n" + str(i) + " page: "
	kaist_notice_list(i)