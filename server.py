import SimpleHTTPServer
import SocketServer
import sys

#f = open("../log/log-serv"+sys.argv[1]+".txt", "a")

class MyHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def handle_one_request(self):
	#ip = self.client_address[0]
	#print(ip)
        #f.write("IP:"+ip+"\n")
        return SimpleHTTPServer.SimpleHTTPRequestHandler.handle_one_request(self)

print("Serving local directory")
httpd = SocketServer.TCPServer(("", 8080), MyHandler)

while True:
    httpd.handle_request()
