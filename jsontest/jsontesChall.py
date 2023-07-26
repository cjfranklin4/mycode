#!/usr/bin/env python 3
import requests as req
import json
import datetime

POSTURL = "http://validate.jsontest.com/"
time_url = 'http://date.jsontest.com/'
ip_url = 'http://ip.jsontest.com/'

def main():
# PART A
    print("Part A")
    current_time = req.get(time_url).json()
    print(f"Current Date and Time is: {current_time['date']} {current_time['time']}")

    # Part B
    print("Part B")
    ip_addr = req.get(ip_url).json()
    print(f"My IP Address is: {ip_addr['ip']}")

    # Part C
    print("Part C")
    server_list = []
    with open("myservers.txt","r") as servers:
        for server in servers:
            new_server = server.rstrip('\n').lstrip()
            server_list.append(new_server)
    print(server_list)

    # Part D
    print("Part D")
    post_data = {"json":"time: {current_time}, ip: {ip_addr}, mysvrs: {server_list}"}
    print(post_data)

if __name__ == "__main__":
    main()
