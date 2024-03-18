"""
A first simple Cloud Foundry Flask app

"""
from flask import Flask, send_from_directory
import os

app = Flask(__name__, static_folder='static')  

# Get port from environment variable or choose 9099 as local default
port = int(os.getenv("PORT", 9099))

@app.route('/')
def hello_world():
    return send_from_directory(app.static_folder, "index.html")

if __name__ == '__main__':
    # Run the app, listening on all IPs with our chosen port number
    app.run(host='0.0.0.0', port=port)