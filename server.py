from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import requests

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        if self.path == '/queueData':
            start = time.time()
            try:
                data = requests.get('https://canteen.nush.app/queueData').json()
                end = time.time()
                self.wfile.write(bytes(f'canteen_raw_count {data["raw_count"]}\n', 'utf-8'))
                self.wfile.write(bytes(f'canteen_sensor_time {data["time"]}\n', 'utf-8'))
                self.wfile.write(bytes(f'canteen_query_time {end-start}\n', 'utf-8'))
            except Exception as e:
                print(e)
        else:
            self.wfile.write(bytes(f'invalid endpoint', 'utf-8'))

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
