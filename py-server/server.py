from http.server import BaseHTTPRequestHandler, HTTPServer

from reader import readFile
from pdfReader import readPDFFile

hostName = "localhost"
serverPort = 8081

class Server(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/read':
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length)

            res = readFile(body.decode("utf-8"))

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes(res, "utf-8"))
        if self.path == '/readPDF':
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length)

            res = readPDFFile(body.decode("utf-8"))

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes(res, "utf-8"))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"404 Not Found")

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), Server)
    print("Python server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Python server stopped.")