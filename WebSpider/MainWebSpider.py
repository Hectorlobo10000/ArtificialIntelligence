import urllib2 as sensor
import re

def getWebContent(text):
    content = sensor.urlopen(url).read()
    valid = re.compile("\\d")
    return valid.match(text)

url = "https://docs.python.org/2/library/re.html"
text = "1"
print getWebContent(text)
