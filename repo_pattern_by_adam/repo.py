from data import Vehicle, Inventory

current_inventory = Inventory()

def retrieve_inventory_list():
    retrieved = current_inventory.read_inventory()
    return retrieved if retrieved else "No vehicles in inventory"

def retrieve_vehicle(index):
    return current_inventory.get_vehicle(index)

def add_vehicle(make, model, year, vin, price):
    return "Added Vehicle" if current_inventory.add_vehicle(make, model, year, vin, price) else "Error"

def modify_vehicle(index, make, model, year, vin, price):
    data = {
        "make": make,
        "model": model,
        "year": year,
        "vin": vin,
        "price": price
    }
    return "Vehicle successfully modified" if current_inventory.modify_vehicle(index, data) else "Error"