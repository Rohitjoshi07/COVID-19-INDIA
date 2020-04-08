import requests
import datetime
import json
import pandas
import frontend
from frontend import *
my= requests.get("https://api.apify.com/v2/key-value-stores/toDWvRj1JpTXiM8FF/records/LATEST?disableRedirect=true")


data=my.json()
def totalcases():
    return data["totalCases"]
def activecases():
    return data["activeCases"]
def deaths():
    return data["deaths"]
def recovered():
    return data["recovered"]
def time():
    return str(data["lastUpdatedAtApify"])