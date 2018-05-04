import urllib2,json,base64
accesstoken="17PSGGC0GJNY1JFA"
institution="10007772"
page=0
url="http://data.unistats.ac.uk/api/v4/KIS/Binstitution.json"
request=urllib2.Request(url)
request.add_header(
	
	"Basic "+ base64.encodestring(accesstoken+":").replace('\n','')
	)
response=urllib2.urlopen(request)
data=json.load(response)
for c in data:
    print c['UKPRN'],c['Name']
