import requests
import sys

i = 100
f = open("log-" + sys.argv[1] + ".txt", "a")
while i > 0:
	x = requests.get('http://10.0.0.5:8080')
	f.write(str(x.elapsed.total_seconds())+"\n")
	i = i - 1

