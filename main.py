# This is a sample Python script.

import pandas as pd
from pandas import json_normalize
import requests


def SaveResultsAsXLS(resultsAsJson):
    df_json = json_normalize(resultsAsJson)
    print(df_json)
    df_json.to_csv('out.csv')


def MakeSearch():
    url = "https://zillow-com1.p.rapidapi.com/propertyExtendedSearch"

    querystring = {
        "location": "santa monica, ca",
        "home_type": "Houses",
        "page": '20'
    }

    headers = {
        "X-RapidAPI-Key": "9d8c020f4cmsh1b21a9eaa87ea22p1abafejsn135b7e4dd5ae",
        "X-RapidAPI-Host": "zillow-com1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    SaveResultsAsXLS(response.json()["props"])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    MakeSearch()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
