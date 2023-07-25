#!/usr/bin/env python 3
import requests
import datetime
import reverse_geocoder as rg

#API Url
url= 'http://api.open-notify.org/iss-now.json'

def main():
    # Call ISS API
    try:
        iss_loc = requests.get(url).json()
    except:
        print("API error")

    #Convert timestamp to Epoch time
    iss_time = iss_loc['timestamp']
    actual_time = datetime.datetime.fromtimestamp(iss_time).strftime('%Y-%m-%d %H:%M:%S')

    #City/Country Location conversion
    iss_lat = iss_loc['iss_position']['latitude']
    iss_lon = iss_loc['iss_position']['longitude']
    
    coords_tuple = (iss_lat, iss_lon)
    loc_res = rg.search(coords_tuple, verbose=False)
    
    city = loc_res[0]['name']
    country = loc_res[0]['cc']
    
    #Print Output
    print("Current Location of the ISS:")
    print(f"Timestamp: {actual_time}")
    print(f"Lat:{iss_loc['iss_position']['latitude']}")
    print(f"Lon:{iss_loc['iss_position']['longitude']}")
    print(f"City/Country: {city}/{country}")

main()
