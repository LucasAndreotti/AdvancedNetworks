#!/usr/bin/env python3

import sys
import datetime
import socket
import json

def get_revenue():
    f = open('logs.json')
    data = json.load(f)
    # print(data)
    f.close()
    return data['revenue']

def get_total_orders():
    f = open('logs.json')
    data = json.load(f)
    # print(data)
    f.close()
    return data['totalOrders']

def main():

    with open("agent.log", 'a') as file:
        file.write(' '.join(sys.argv)+"\n")

    # readJson()
    if len(sys.argv) != 3:
        print("Usage: agent.py <request-type> <MIB-oid>")
        return

    request_type = sys.argv[1]
    oid = sys.argv[2]

    if request_type == "-g":  # GET request # -s é set, -g 
        if oid == ".1.3.6.1.3.1234.1.1.0":
            print(".1.3.6.1.3.1234.1.1.0")
            print("integer")
            print(get_revenue())
        elif oid == ".1.3.6.1.3.1234.1.2.0":
            print(".1.3.6.1.3.1234.1.2.0")
            print("integer")
            print(get_total_orders())
        else:
            print("NONE")
    else:
        print("NONE")

if __name__ == "__main__":
    main()

