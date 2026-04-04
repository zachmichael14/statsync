import os

from urllib.parse import urlencode

from dotenv import load_dotenv
from flask import Flask
import requests

app = Flask(__name__)


@app.route("/")
def index():
    params = {
        "client_id": os.getenv("CLIENT_ID"),
        "redirect_uri": f"{os.getenv('DOMAIN_URI')}/home",
        "response_type": "code",
        "scope": "activity:read_all,profile:read_all"
    }
    auth_url = "https://www.strava.com/oauth/authorize?" + urlencode(params)
    return f'''
        <html>
            <body>
                <a href="{auth_url}">
                    <button>Login with Strava</button>
                </a>
            </body>
        </html>
    '''

@app.route("/home")
def home():
    return"<p>I'm a placeholder!</p>"


if __name__ == "__main__":
    load_dotenv()
    app.run()