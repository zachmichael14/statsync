import os

from urllib.parse import urlencode

from dotenv import load_dotenv
from flask import Flask, redirect, request, session, url_for
import requests

app = Flask(__name__)


@app.route("/")
def index():
    params = {
        "client_id": os.getenv("CLIENT_ID"),
        "redirect_uri": f"{os.getenv('DOMAIN_URI')}/auth",
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

@app.route("/auth")
def auth():
    auth_code = request.args.get("code")

    request_body = {
        "client_id": os.getenv("CLIENT_ID"),
        "client_secret": os.getenv("CLIENT_SECRET"),
        "code": auth_code,
        "grant_type": "authorization_code"
    }

    response = requests.post(
        "https://www.strava.com/oauth/token",
        data=request_body
    ).json()


    session["access_token"] = response.get("access_token")
    session["refresh_token"] = response.get("refresh_token")

    if all([session["access_token"], session["refresh_token"]]):
        name = f"{response.get("firstname")}_{response.get("lastname")}"
        return redirect(url_for("athlete_home"), athlete=name)
    
    return f"Auth failed, how very sad."

@app.route("/home/{athlete}")
def athlete_home():
    return "foo"






if __name__ == "__main__":
    load_dotenv()
    app.secret_key = os.getenv("APP_SECRET").encode("UTF-8")
    app.run()