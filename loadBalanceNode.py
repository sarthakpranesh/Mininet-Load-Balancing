import SimpleHTTPServer
import SocketServer


class MyHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
   def do_GET(self):
       self.send_response(301)
       self.send_header('Location', 'http://10.0.0.5:8080')
       self.end_headers()


pywebserver = SocketServer.TCPServer(("", 9090), MyHandler)

pywebserver.serve_forever()
