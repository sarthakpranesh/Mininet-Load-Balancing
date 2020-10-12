import requests
import sys

i = 100
f = open("./log/log-" + sys.argv[1] + ".txt", "a")
while i > 0:
	x = requests.get('http://192.168.56.101:9090')
	f.write(str(x.elapsed.total_seconds())+"\n")
	i = i - 1


