import urllib2,json,base64
accesstoken="17PSGGC0GJNY1JFAL5Y5"
url="http://data.unistats.ac.uk/api/v4/KIS/Institutions.json"
request=urllib2.Request(url)
request.add_header(
	"Authorization",
	"Basic "+ base64.encodestring(accesstoken+":").replace('\n','')
	)
response=urllib2.urlopen(request)
data=json.load(response)
print data['Name']
