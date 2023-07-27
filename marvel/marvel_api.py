#!/usr/bin/env python 3
import requests
import hashlib
import time
from dotenv import load_dotenv
import os
import argparse
from pprint import pprint

#Import keys
load_dotenv()
PRIV_KEY = os.getenv("marvel_api_priv")
PUB_KEY = os.getenv("marvel_api_pub")

def hash_builder():
    #Get timestamp
    ts = time.time()
    ts = str(ts)

    #md5 hasing
    pre_hash = ts + PRIV_KEY + PUB_KEY
    hash_str = hashlib.md5(pre_hash.encode())
    hash_str = hash_str.hexdigest()

    # request url
    url = 'http://gateway.marvel.com/v1/public/characters?ts=' + ts + '&apikey=' + PUB_KEY + '&hash=' + hash_str

    #print(url)
    return url

#base_url = hash_builder()

## Perform a call to MARVEL Character API
## http://gateway.marvel.com/v1/public/characters
## ?name=Spider-Man&ts=1&apikey=1234&hash=ffd275c5130566a2916217b101f26150
def marvelcharcall(url, lookmeup):
    r = requests.get(f"{url}&name={lookmeup}")  # send an HTTP GET to this location

    # the marvel APIs are "flakey" at best, so check for a 200 response
    if r.status_code != 200:
        response = None     #
    else:
        response = r.json()

    # return the HTTP response with the JSON removed
    return response

def main():
    base_url = hash_builder()
    print(base_url)

    #get character from args
    char = args.hero
    print(char, "char")

    res = marvelcharcall(base_url, char)
    pprint(res)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--hero', help='Character to search for in the Marvel API')
    args = parser.parse_args()
    main()
