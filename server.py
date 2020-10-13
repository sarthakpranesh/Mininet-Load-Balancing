import SimpleHTTPServer
import SocketServer
import sys
import time


class MyHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def handle_one_request(self):
	time.sleep(0.1)	
        return SimpleHTTPServer.SimpleHTTPRequestHandler.handle_one_request(self)

print("Serving local directory")
httpd = SocketServer.TCPServer(("", 8080), MyHandler)

while True:
    httpd.handle_request()
