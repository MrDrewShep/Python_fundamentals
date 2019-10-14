from datetime import datetime

class Vehicle:

    def __init__(self, make, model, year, vin, list_price):
        self.make = make
        self.model = model
        self.year = year
        self.vin = vin
        self.list_price = list_price
        self.date_added = datetime.now()
        self.date_modified = datetime.now()

    def __repr__(self):
        return f'< CAR: { self.make }, { self.model }, { self.year }, { self.vin }, { self.list_price } >'

    def __str__(self):
        return f'< CAR: { self.make }, { self.model }, { self.year }, { self.vin }, { self.list_price } >'
    
    def change_year(self, new_year):
        self.year = new_year
        self.date_modified = datetime.now()
        return 1
    
    def change_make(self, new_make):
        self.make = new_make
        self.date_modified = datetime.now()
        return 1

    def change_model(self, new_model):
        self.model = new_model
        self.date_modified = datetime.now()
        return 1

    def change_vin(self, new_vin):
        self.vin = new_vin
        self.date_modified = datetime.now()
        return 1

    def change_price(self, new_price):
        self.list_price = new_price
        self.date_modified = datetime.now()
        return 1


class Inventory:

    def __init__(self, previous_inventory=[]):
        self.vehicles = previous_inventory
        self.date_created = datetime.now()
        self.date_modified = datetime.now()
    
    def __repr__(self):
        return f'< Inventory: { len(self.vehicles ) } cars >'
    
    def add_vehicle(self, make, model, year, vin, price):
        new_vehicle = Vehicle(make, model, year, vin, price)
        self.vehicles.append(new_vehicle)
        self.date_modified = datetime.now()
        return 1
    
    def get_vehicle(self, index):
        try:
            vehicle = self.vehicles[index]
        except IndexError:
            vehicle = "Vehicle not found"
        return vehicle

    def modify_vehicle(self, index, data):
        to_change = self.vehicles[index]
        for key in data:
            # In order to have a long chain of if and elif statments, I can modularly call what function I need
            # based on the name of the key. Check out the getattr function. Notice how I call what comes back
            getattr(to_change, f'change_{key}')(data[key]) if data[key] else None
            
        return 1

    def read_inventory(self):
        message = ""
        if len(self.vehicles):
             message += "ID  Make,  Model,  Year\n"
        for index, vehicle in enumerate(self.vehicles):
            message += f"{ index } - { vehicle.make }, { vehicle.model }, { vehicle.year }\n"
        return message

#hw getattr function