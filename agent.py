import sys
import datetime
import socket
import json

# PATH = '/workspaces/RedesAvancT2/'
PATH = '/workspaces/AdvancedNetworks/'

def readJson(obj):
    f = open(PATH+'logs.json')
    data = json.load(f)
    f.close
    return data[obj]

#get
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
    return readJson('sandwich')

def get_pie():
    return readJson('pie')

def get_status():
    return readJson('status')

def get_employee(index):
    return readJson('employees')[index]

#set
def set_status(new_status):
    filepath = PATH + 'status.txt'
    with open(filepath, 'w+') as f:
        f.write(new_status)
    return new_status

def main():

    with open(PATH+"agent.log", 'a') as file:
        file.write(' '.join(sys.argv)+"\n")

    # readJson()
    if len(sys.argv) < 3:
        print("Usage: agent.py <request-type> <MIB-oid>")
        return

    request_type = sys.argv[1]
    oid = sys.argv[2]

    if request_type == "-g":  # GET request  
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
        #employeeId
        elif oid == ".1.3.6.1.3.1234.1.10.1.1" or oid == ".1.3.6.1.3.1234.1.10.1.1.1": 
            print(".1.3.6.1.3.1234.1.10.1.1.1")
            print("integer")
            print(1)
        elif oid == ".1.3.6.1.3.1234.1.10.1.1.2":
            print(".1.3.6.1.3.1234.1.10.1.1.2")
            print("integer")
            print(2)
        elif oid == ".1.3.6.1.3.1234.1.10.1.1.3":
            print(".1.3.6.1.3.1234.1.10.1.1.3")
            print("integer")
            print(3)
        #employeeName
        elif oid == ".1.3.6.1.3.1234.1.10.1.2" or oid == ".1.3.6.1.3.1234.1.10.1.2.1": 
            print(".1.3.6.1.3.1234.1.10.1.2.1")
            print("string")
            print(get_employee(0))
        elif oid == ".1.3.6.1.3.1234.1.10.1.2.2":
            print(".1.3.6.1.3.1234.1.10.1.2.2")
            print("string")
            print(get_employee(1))
        elif oid == ".1.3.6.1.3.1234.1.10.1.2.3":
            print(".1.3.6.1.3.1234.1.10.1.2.3")
            print("string")
            print(get_employee(2))

        # elif oid == ".1.3.6.1.3.1234.1.10.2.1": #não existe
        #     print(".1.3.6.1.3.1234.1.10.2.1")
        #     print("integer")
        #     print(2)
        # elif oid == ".1.3.6.1.3.1234.1.10.2.2":
        #     print(".1.3.6.1.3.1234.1.10.2.2")
        #     print("string")
        #     print(get_employee(1))
        # elif oid == ".1.3.6.1.3.1234.1.10.3.1":
        #     print(".1.3.6.1.3.1234.1.10.3.1")
        #     print("integer")
        #     print(3)
        # elif oid == ".1.3.6.1.3.1234.1.10.3.2":
        #     print(".1.3.6.1.3.1234.1.10.3.2")
        #     print("string")
        #     print(get_employee(2))
        else:
            print("NONE")

    elif request_type == "-s":  # SET request
        if oid == ".1.3.6.1.3.1234.1.9.0" and len(sys.argv) == 5: # agent.py <request-type> <MIB-oid> [type] [<new-value>]
            new_status = sys.argv[4]
            print(".1.3.6.1.3.1234.1.9.0")
            print("string")
            print(set_status(new_status))
        else:
            print("NONE")
    
    elif request_type == "-n":  # GETNEXT request  
        if oid == ".1.3.6.1.3.1234.1.1":
            print(".1.3.6.1.3.1234.1.1.0")
            print("integer")
            print(get_revenue())
        elif oid == ".1.3.6.1.3.1234.1.1.0" or oid == ".1.3.6.1.3.1234.1.2":
            print(".1.3.6.1.3.1234.1.2.0")
            print("integer")
            print(get_total_orders())
        elif oid == ".1.3.6.1.3.1234.1.2.0" or oid == ".1.3.6.1.3.1234.1.3":
            print(".1.3.6.1.3.1234.1.3.0")
            print("integer")
            print(get_coffee())
        elif oid == ".1.3.6.1.3.1234.1.3.0" or oid == ".1.3.6.1.3.1234.1.4":
            print(".1.3.6.1.3.1234.1.4.0")
            print("integer")
            print(get_tea())
        elif oid == ".1.3.6.1.3.1234.1.4.0" or oid == ".1.3.6.1.3.1234.1.4":
            print(".1.3.6.1.3.1234.1.5.0")
            print("integer")
            print(get_soda())
        elif oid == ".1.3.6.1.3.1234.1.5.0" or oid == ".1.3.6.1.3.1234.1.6":
            print(".1.3.6.1.3.1234.1.6.0")
            print("integer")
            print(get_muffin())
        elif oid == ".1.3.6.1.3.1234.1.6.0" or oid == ".1.3.6.1.3.1234.1.7":
            print(".1.3.6.1.3.1234.1.7.0")
            print("integer")
            print(get_sandwich())
        elif oid == ".1.3.6.1.3.1234.1.7.0" or oid == ".1.3.6.1.3.1234.1.8":
            print(".1.3.6.1.3.1234.1.8.0")
            print("integer")
            print(get_pie())
        elif oid == ".1.3.6.1.3.1234.1.8.0" or oid == ".1.3.6.1.3.1234.1.9":
            print(".1.3.6.1.3.1234.1.9.0")
            print("string")
            print(get_status())
        elif oid == ".1.3.6.1.3.1234.1.10.1" or oid == '.1.3.6.1.3.1234.1.10' or oid == ".1.3.6.1.3.1234.1.9.0":
            print(".1.3.6.1.3.1234.1.10.1.1")
            print("integer")
            print(1)
        elif oid == ".1.3.6.1.3.1234.1.10.3.1":
            print(".1.3.6.1.3.1234.1.10.1.2")
            print("string")
            print(get_employee(0))
        elif oid == ".1.3.6.1.3.1234.1.10.1.1" or oid == ".1.3.6.1.3.1234.1.10.2":
            print(".1.3.6.1.3.1234.1.10.2.1")
            print("integer")
            print(2)
        elif oid == ".1.3.6.1.3.1234.1.10.1.2":
            print(".1.3.6.1.3.1234.1.10.2.2")
            print("string")
            print(get_employee(1))
        elif oid == ".1.3.6.1.3.1234.1.10.2.1" or oid == ".1.3.6.1.3.1234.1.10.3":
            print(".1.3.6.1.3.1234.1.10.3.1")
            print("integer")
            print(3)
        elif oid == ".1.3.6.1.3.1234.1.10.2.2":
            print(".1.3.6.1.3.1234.1.10.3.2")
            print("string")
            print(get_employee(2))
        else:
            print("NONE")

    else:
        print("NONE")

if __name__ == "__main__":
    main()


# get test 
# sudo python agent.py -g .1.3.6.1.3.1234.1.9.0

# set test
# sudo python agent.py -s .1.3.6.1.3.1234.1.9.0 s teste
# snmpset -v2c -c private localhost .1.3.6.1.3.1234.1.9.0 s teste