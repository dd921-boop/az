import logging
from flask import request

# Set up logging to Vercel logs
logging.basicConfig(level=logging.INFO)

@app.route('/your-endpoint', methods=['GET', 'POST'])
def your_endpoint():
    visitor_ip = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    logging.info(f'Visitor IP: {visitor_ip}, User Agent: {user_agent}')
    # Your code logic here
    return 'Logged IP and User Agent', 200
