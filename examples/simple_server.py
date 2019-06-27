
import http
import os
from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import ThreadingMixIn

# http.server.HTTPServer
# http.server.BaseHTTPRequestHandler

class ServerProcessor(BaseHTTPRequestHandler):
    def do_GET(self):
        root_dir = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')
        
        print('GET, path: ', self.path, ' ; ', root_dir)
        rfile = self.path[1:]
        if(rfile in ['server_tester.html', 'jquery3.js']):
            print('file requested')
            file_path = root_dir + '/web-files/' + rfile
            with open(file_path, 'r') as rstream:
                text = rstream.read()
                return self.send_response_ok(text)

        print('GET request...')
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        target_path=''
        query = ''
        

        text = '''test hello!
        path: {},
        command: {}'''.format(self.path, self.command)
        self.wfile.write(bytes(text, 'utf-8'))
    
    def send_response_ok(self, text):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes(text, 'utf-8'))

class MultithreadHttpServer(ThreadingMixIn, HTTPServer):
    '''>> Hanlde requests in separate threads
    https://stackoverflow.com/questions/14088294/multithreaded-web-server-in-python
    '''

# serv = HTTPServer(('localhost', 81), ServerProcessor)
serv = MultithreadHttpServer(('localhost', 81), ServerProcessor)
serv.serve_forever()

