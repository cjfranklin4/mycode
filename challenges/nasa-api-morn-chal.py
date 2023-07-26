#!/usr/bin/env python3
import requests

birthdate_url = 'https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&date=2020-01-13'

class_range_url = 'https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&start_date=2023-07-17&end_date=2023-07-21'

random_url = 'https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY%count=1'

def main():
    res = requests.get(birthdate_url).json()
    print(res)
main()
