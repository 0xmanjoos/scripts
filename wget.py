import urllib2
import time

max_attempts = 80
attempts = 0
sleeptime = 10 #in seconds, no reason to continuously try if network is down

#while true: #Possibly Dangerous
while attempts < max_attempts:
    time.sleep(sleeptime)
    try:
        response = urllib2.urlopen("http://example.com", timeout = 5)
        content = response.read()
        f = open( "local/index.html", 'w' )
        f.write( content )
        f.close()
        break
    except urllib2.URLError as e:
        attempts += 1
        print type(e)
