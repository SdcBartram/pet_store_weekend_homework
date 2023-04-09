
def get_pet_shop_name(cc_pet_shop):
    return cc_pet_shop["name"]

def get_total_cash(cc_pet_shop):
    return cc_pet_shop["admin"]["total_cash"]

def add_or_remove_cash(cc_pet_shop, amount):
    cc_pet_shop["admin"]["total_cash"] += amount

def get_pets_sold(cc_pet_shop):
    return cc_pet_shop["admin"]["pets_sold"]

def increase_pets_sold(cc_pet_shop, sales):
    cc_pet_shop["admin"]["pets_sold"] += sales
    return cc_pet_shop["admin"]["pets_sold"]

def get_stock_count(cc_pet_shop):
    return len(cc_pet_shop["pets"])

def get_pets_by_breed(cc_pet_shop, breed):
    total_pets_by_breed = []
    for pet in cc_pet_shop["pets"]:
        if pet["breed"] == breed:
            total_pets_by_breed.append(pet)
    return total_pets_by_breed

def find_pet_by_name(cc_pet_shop, name):
    pets = cc_pet_shop["pets"]
    for pet in pets:
        if pet["name"] == name:
            return pet
        
def remove_pet_by_name(cc_pet_shop, name):
    for pet in cc_pet_shop["pets"]:
        if pet["name"] == name:
            cc_pet_shop["pets"].remove(pet)

def add_pet_to_stock(cc_pet_shop, pet):
    cc_pet_shop["pets"].append(pet)

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, remove_cash_amount):
    customer["cash"] -= remove_cash_amount

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)

def customer_can_afford_pet(customer, new_pet):
    customer_cash = customer["cash"]
    cost_of_new_pet = new_pet["price"]
    return customer_cash >= cost_of_new_pet

def sell_pet_to_customer(cc_pet_shop, pet, customer):
    #pet name not found ---> condition needed
    if pet in cc_pet_shop["pets"]:
        # check balance of customer cash
        if customer_can_afford_pet(customer, pet):
            # first remove pet from stock
            remove_pet_by_name(cc_pet_shop, pet["name"])
            # add pet to customers pet count
            add_pet_to_customer(customer, pet)
            # customer cash decreases
            remove_customer_cash(customer, pet["price"])
            # increase admin cash amount
            add_or_remove_cash(cc_pet_shop, pet["price"])
            # increase admin numeber of sales/pets sold
            increase_pets_sold(cc_pet_shop, 1)



