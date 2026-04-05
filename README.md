# StatSync
A visualizer for personal fitness data

## Table of Contents

- [StatSync](#statsync)
  - [Overview](#overview)
  - [Usage & Installation](#usage--installation)
  - [Setup (Linux Notes)](#setup-linux-notes)
    - [1. Strava Authorization](#1-strava-authorization)
      - [a. Create Strava Application](#a-create-strava-application)
      - [b. Retrieve Client Credentials](#b-retrieve-client-credentials)
    - [2. Installing Software](#2-installing-software)
      - [a. Install Python](#a-install-python)
      - [b. Create Virtual Environment](#b-create-virtual-environment)
      - [c. Install Dependencies](#c-install-dependencies)
      - [d. Configure Environment Variables](#d-configure-environment-variables)
  - [TODO](#todo)
  - [Future Directions](#future-directions)

---

## Overview
A visualizer for personal fitness data.

## Usage 
Usage GIFs and such coming soon. Maybe.

## Setup (Linux Notes)

I've included basic Linux set up instructions below as much to remind myself as anything else, so your mileage may vary.

### 1. Strava Authorization

#### a. Create Strava Application
Create an application in your Strava account by following the guide [here](https://developers.strava.com/docs/getting-started/#account)

- Since this app runs locally at the moment:
  - `Website`: `http://localhost`
  - `Authorization Callback Domain`: `localhost`

#### b. Retrieve Client Credentials
You will need the Client ID and Client Secret from the step above before moving forward.

### 2. Installing Software

#### a. Install Python
[Install Python](https://realpython.com/installing-python/) if not yet installed.

#### b. Create Virtual Environment
Create a virtual environment inside the same directory containing the app.
```bash
# create virtual environment
python3 -m venv .venv
```

#### c. Install Dependencies
Install dependencies in the activated virtual environment.
```bash
source .venv/bin/activate

pip install -r requirements.txt
```


#### d. Configure Environment Variables
Create a `.env` file populated with Client ID and Client Secret from Strava.

First, create a .env file
```bash
touch .env
```

Then, generate an app secret and write that to the .env file

```bash
echo "APP_SECRET=$(python -c 'import secrets; print(secrets.token_hex())')" >> .env
```

Then, write Client ID and Client Secret the same file
```bash
echo CLIENT_ID=<YOUR_CLIENT_ID> >> .env
echo CLIENT_SECRET=<YOUR_CLIENT_SECRET> >> .env
```

## TODO (no particular order)

- [DONE] ~~Auth~~
- [DONE] ~~Create home/dash/profile page~~
- Links to pull in data from all time/date range
    - To avoid pulling data that was fetched previously, storing a last_updated_date somewhere and only querying for activities after that date could work.
- Populate athlete profile page with data
  - This will also entail coming up with stats to include/calculate. It may make sense for this to be broken up into tabs/sections, but a single dashboard will suffice as an  
    MVP.
- [DONE] ~~Redirect to home after auth~~
  - ~~Currently, the user is left on auth page, redirect to a dashboard or profile page or something~~
- Cache/store data
  - Possibly two methods: CSV and SQLite.
  - SQLite is lightweight enough to store locally and makes for nice filtering.
  - CSV is convenient and easy to process.
  - Both make data available offline and help prevent unnecessary API requests.
  - Caching could be useful but may not be necessary
- 
---

## Future Directions

- Enable writing/editing