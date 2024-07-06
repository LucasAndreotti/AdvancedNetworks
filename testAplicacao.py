from random import randrange
import time
import json

# Funcionários
employees = ["Gabriela","Joana","Lucas"]

# Items
items = ["coffee","tea","soda","muffin","sandwich","pie"]

# Número items
itemsNumber = [0,0,0,0,0,0]

# Tabela de preços
priceTable = {"coffee" : 8, "tea" : 5, "soda" : 6, "muffin" : 7, "sandwich" : 15, "pie" : 12 }

# Número pedidos
orders = 0

# Total valor
totalValue = 0

# Status
status = "Open"


while(True):
    index = randrange(0,5)
    item = items[index]
    value = priceTable[item]

    orders += 1
    totalValue += value
    itemsNumber[index] += 1

    log = {
        "revenue" : totalValue,
        "totalOrders" : orders,
        items[0] : itemsNumber[0],
        items[1] : itemsNumber[1],
        items[2] : itemsNumber[2],
        items[3] : itemsNumber[3],
        items[4] : itemsNumber[4],
        items[5] : itemsNumber[5],
        "employees" : employees,
        "priceTable" : priceTable,
        "status" : status
    }

    # print(log)
   
    json_object = json.dumps(log, indent=4)
    
    with open("/workspaces/AdvancedNetworks/logs.json", "w") as outfile:
        outfile.write(json_object)
        outfile.close()

    time.sleep(10)