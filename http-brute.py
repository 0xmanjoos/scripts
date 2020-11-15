#!/usr/bin/env python3
import os, requests, time, sys, signal
try:
    url = sys.argv[1]
    wordlist = sys.argv[2]

    file = open(wordlist, "r")
    for link in file.read().splitlines():
        final = url + "/" +link
        r = requests.get(final)
        if r.status_code == 200 or r.status_code == 300:
            print("Found at ", final)
        else:
            pass
except KeyboardInterrupt:

    print("Ctrl + C pressed!")
    time.sleep(1)
    print("Thanks for your time")

except:
    print("Usage python3 %s [URL] [WORDLIST]" % (sys.argv[0]))
