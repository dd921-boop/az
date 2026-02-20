import requests
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        url = 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fproduction-gameflipusercontent.fingershock.com%2Fus-east-1%3Acae50598-4dbe-4cdd-95a6-63aec990f8e5%2Fbc5bf4ac-f898-4dcd-878b-86c535421d9d%2Fe3c0060b-7d63-46fe-95cb-a75f6c3b4785&f=1&nofb=1&ipt=5a71201f7822cde316832a82afa54c646321c92828e2a8238b95e647d25a0ada'
        
        try:
            response = requests.get(url)
            self.send_response(200)
            self.send_header('Content-type', 'image/jpeg')
            self.end_headers()
            self.wfile.write(response.content)
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(f'Error: {str(e)}'.encode())