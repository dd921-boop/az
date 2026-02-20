import requests
from flask import Flask, send_file

app = Flask(__name__)

@app.route('/cat')
def cat():
    url = 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fproduction-gameflipusercontent.fingershock.com%2Fus-east-1%3Acae50598-4dbe-4cdd-95a6-63aec990f8e5%2Fbc5bf4ac-f898-4dcd-878b-86c535421d9d%2Fe3c0060b-7d63-46fe-95cb-a75f6c3b4785&f=1&nofb=1&ipt=5a71201f7822cde316832a82afa54c646321c92828e2a8238b95e647d25a0ada'
    response = requests.get(url)
    return send_file(response.raw, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)