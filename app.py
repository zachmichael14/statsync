import csv
import io
import os


import pandas as pd
from urllib.parse import urlencode

from dotenv import load_dotenv
from flask import Flask, Response, redirect, render_template, request, session, url_for
import requests

BASE_URL="https://www.strava.com/api/v3"
AUTH_URL="https://www.strava.com/oauth/authorize?"
TOKEN_URL="https://www.strava.com/oauth/token"

app = Flask(__name__)


@app.route("/")
def index():
    params = {
        "client_id": os.getenv("CLIENT_ID"),
        "redirect_uri": f"{os.getenv('DOMAIN_URI')}/auth",
        "response_type": "code",
        "scope": "activity:read_all,profile:read_all"
    }
    auth_url = AUTH_URL + urlencode(params)
    return render_template("index.html", auth_url=auth_url)
   
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
        TOKEN_URL,
        data=request_body
    ).json()

    session["access_token"] = response.get("access_token")
    session["refresh_token"] = response.get("refresh_token")

    if all([session["access_token"], session["refresh_token"]]):
        athlete = response.get("athlete", {})
        session["athlete_id"] = athlete.get("id")
        name = f"{athlete.get("firstname")}_{athlete.get("lastname")}"
        return redirect(url_for("athlete_home", athlete_name=name))
    
    return f"Auth failed, how very sad."

@app.route("/home/<athlete_name>")
def athlete_home(athlete_name):
    athlete_names = athlete_name.split("_")
    return render_template("athlete.html", athlete_name=athlete_names[0])

@app.route("/activities")
def activities():

    header = {
        "Authorization": f"Bearer {session['access_token']}"
    }

    params = {
        "page": 3,
        "per_page": 100,
    }
    list_activity_url = f"{BASE_URL}/athlete/activities"


    response = requests.get(
        list_activity_url,
        params=params,
        headers=header
    ).json()
    
   
    df = pd.DataFrame(response)

    return Response(
        df.to_csv(index=False),
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment; filename=activities.csv"}
    )




if __name__ == "__main__":
    load_dotenv()
    app.secret_key = os.getenv("APP_SECRET").encode("UTF-8")
    app.run()