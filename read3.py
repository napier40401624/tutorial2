import urllib2,json,base64
accesstoken="17PSGGC0GJNY1JFAL5Y5"
institution="10007772"
course="U56119"
page=0
url="http://data.unistats.ac.uk/api/v4/KIS/Institution/{}/Course/{}/FullTime/Statistics.json".format(institution,course)
request=urllib2.Request(url)
request.add_header(
	"Authorization",
	"Basic "+ base64.encodestring(accesstoken+":").replace('\n','')
	)
response=urllib2.urlopen(request)
data=json.load(response)

aa=data[6]["Details"]
cc=aa[4]["Value"]
dd=aa[1]["Value"]
ee=data[5]["Details"]
ff=ee[0]["Value"]
print cc
print dd
print ff
