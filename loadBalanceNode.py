import SimpleHTTPServer
import SocketServer
import sys
import random

def RR(c, arr):
	if (c % 2 == 0):
		add = arr[0]
	else:
		add = arr[1]
	return add

def Random(arr):
	n = random.randint(0,1)
	return arr[n]

class MyHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
	arr = ["http://10.0.0.5:8080", "http://10.0.0.6:8080"]	
        
	def do_GET(self):
		global c
		self.send_response(301)
		if (sys.argv[1] == "bal"):
			add = Random(self.arr)
		else:
			add = self.arr[0]
		c = c + 1
		#print(add)
		self.send_header('Location', add)
		self.end_headers()

c = 0

pywebserver = SocketServer.TCPServer(("", 9090), MyHandler)

pywebserver.serve_forever()
