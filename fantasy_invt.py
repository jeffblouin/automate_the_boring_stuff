#This fct will print the items and quantity of each item in inventory
#It take a dictionnry and print each item with the numbers in inventory
import pprint
stuff = {"rope":1, "torch": 6, "gold": 42, "dagger":1}

def displayInvent(inventory):
    total_items = 0
    for k, v in inventory.items():
        print(f"{v} {k}")
        total_items += v
    print("Total number of items: " + str(total_items))

displayInvent(stuff)

# This fct tale a loot(dict) and add it to the existing inventory(dict)
def addToInventory(inventory, addeditems): 
  
    for k,v in addeditems.items():
        if k in inventory.keys():
            inventory[k] += v
        inventory.setdefault(k,v)
  
 #other way to do it with get method

    # for k,v in addeditems.items():
    #     x = inventory.get(k,0)
    #     if x == 0:
    #         inventory[k] = v
    #     else:
    #         inventory[k] += v   
        
        

      
    pprint.pprint(inventory)

inv = {"gold": 5, "shield":100} 
dragon_loot = {"gold":5, "sword": 2}

addToInventory(inv,dragon_loot)


