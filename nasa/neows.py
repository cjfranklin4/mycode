#!/usr/bin/python3
import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")
#print(api_key)

## Define NEOW URL
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

# this function grabs our credentials
# it is easily recycled from our previous script
def returncreds():
    ## first I want to grab my credentials
    with open("/home/student/mycode/nasa/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")
    return nasacreds

# this is our main function
def main(key):
    ## first grab credentials
    nasacreds = key
    print(nasacreds)

    ## update the date below, if you like
    #startdate = "start_date=2019-11-11"
    startdate = input("Enter a start date with the formar YYYY-MM-DD:")

    ## the value below is not being used in this
    ## version of the script
    enddate = input("Enter an end date with the format YYY-MM-DD (optional):")
    
    # make a request with the request library
    if enddate == '':
        neowrequest = requests.get(NEOURL + "start_date="+ startdate + "&api_key="  +  nasacreds)
    else:
        print("else")
        neowrequest = requests.get(NEOURL + startdate + "&" + enddate + "&" + nasacreds)

    #print(neowrequest)
    #print(NEOURL + startdate + "&" + nasacreds)
    # strip off json attachment from our response
    neodata = neowrequest.json()

    ## display NASAs NEOW data
    print(neodata)

if __name__ == "__main__":
    main(api_key)

