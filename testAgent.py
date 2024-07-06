import sys
import datetime
import socket
import json

def readJson(obj):
    f = open('/workspaces/AdvancedNetworks/logs.json')
    data = json.load(f)
    f.close
    return data[obj]

def get_revenue():
    return readJson('revenue')

def get_total_orders():
    return readJson('totalOrders')

def get_coffee():
    return readJson('coffee')

def get_tea():
    return readJson('tea')

def get_soda():
    return readJson('soda')

def get_muffin():
    return readJson('muffin')

def get_sandwich():
    return 2

def get_pie():
    return 1

def get_status():
    return "Open"

def get_employees():
    return ["Gabriela","Lucas","Joana"]

def main():

    with open("/workspaces/AdvancedNetworks/agent.log", 'a') as file:
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
        elif oid == ".1.3.6.1.3.1234.1.3.0":
            print(".1.3.6.1.3.1234.1.3.0")
            print("integer")
            print(get_coffee())
        elif oid == ".1.3.6.1.3.1234.1.4.0":
            print(".1.3.6.1.3.1234.1.4.0")
            print("integer")
            print(get_tea())
        elif oid == ".1.3.6.1.3.1234.1.5.0":
            print(".1.3.6.1.3.1234.1.5.0")
            print("integer")
            print(get_soda())
        elif oid == ".1.3.6.1.3.1234.1.6.0":
            print(".1.3.6.1.3.1234.1.6.0")
            print("integer")
            print(get_muffin())
        elif oid == ".1.3.6.1.3.1234.1.7.0":
            print(".1.3.6.1.3.1234.1.7.0")
            print("integer")
            print(get_sandwich())
        elif oid == ".1.3.6.1.3.1234.1.8.0":
            print(".1.3.6.1.3.1234.1.8.0")
            print("integer")
            print(get_pie())
        elif oid == ".1.3.6.1.3.1234.1.9.0":
            print(".1.3.6.1.3.1234.1.9.0")
            print("string")
            print(get_status())
        elif oid == ".1.3.6.1.3.1234.1.10.0":
            print(".1.3.6.1.3.1234.1.10.0")
            print("table")
            print(get_employees())
        else:
            print("NONE")
    else:
        print("NONE")

if __name__ == "__main__":
    main()