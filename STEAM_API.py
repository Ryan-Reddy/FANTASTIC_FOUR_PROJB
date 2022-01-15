"""Section outline:
Create an app list from SteamSpy API using ‘all’ request
Retrieve individual app data from Steam API, by iterating through app list
Retrieve individual app data from SteamSpy API, by iterating through app list
Export app list, Steam data and SteamSpy data to csv files
API references:
https://partner.steamgames.com/doc/webapi
https://wiki.teamfortress.com/wiki/User:RJackson/StorefrontAPI
https://steamapi.xpaw.me/#
https://steamspy.com/api.php
Import Libraries
We begin by importing the libraries we will be using.
We start with standard library imports, or those available by default in Python,
then import the third-party packages.
We’ll be using requests to handle interacting with the APIs,
then the popular pandas and numpy libraries for handling the downloaded data."""

# standard library imports
import csv
import datetime as dt
import json
import os
import statistics
import time

# third-party imports
import numpy as np
import pandas as pd
import requests

# customisations - ensure tables show all columns
pd.set_option("max_columns", 100)

# ---------------------------------------------------------------------------------
def get_request(url, parameters=None):
    """Return json-formatted response of a get request using optional parameters.

    Parameters
    ----------
    url : string
    parameters : {'parameter': 'value'}
        parameters to pass as part of get request

    Returns
    -------
    json_data
        json-formatted response (dict-like)
    """
    try:
        response = requests.get(
            url=url, params=parameters
        )  # <--- try to get a response from the api
    except SSLError as s:  # <--- if no response, answer with print(error) and retry in 5s
        print("SSL Error:", s)

        for i in range(5, 0, -1):
            print("\rWaiting... ({})".format(i), end="")
            time.sleep(1)  # <--- 5 sleeps of 1 sec(really short sleeps)
        print("\rRetrying." + " " * 10)  # <--- retry 10 times :O

        return get_request(
            url, parameters
        )  # <--- and another 10! recusively retry function

    if response:
        return response.json()  # <--- got a response, transform to .json
    else:
        # response is none usually means too many requests. Wait and try again
        print("No response, waiting 10 seconds...")
        time.sleep(10)  # <--- longer sleep this time 10s
        print("Retrying.")
        return get_request(url, parameters)  # <--- and another recursive


# ---------------------------------------------------------------------------------

url = "https://steamspy.com/api.php"
parameters = {"request": "all"}

# request 'all' from steam spy and parse into dataframe
json_data = get_request(url, parameters=parameters)
steam_spy_all = pd.DataFrame.from_dict(json_data, orient="index")

# generate sorted app_list from steamspy data
app_list = steam_spy_all[["appid", "name"]].sort_values("appid").reset_index(drop=True)

# export disabled to keep consistency across download sessions
app_list.to_csv("../data/download/app_list.csv", index=False)
#
# # instead read from stored csv
# app_list = pd.read_csv("../data/download/app_list.csv")

# display first few rows
app_list.head()
