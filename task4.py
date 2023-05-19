import sys
class Vehicle:
   

    def set_vehicleInfo(self, vehicle_type, vehicle_capacity, vehicle_year):
        
        self.type = vehicle_type
        self.capacity = vehicle_capacity
        self.year = vehicle_year

    def set_flag(self, flag):
        self.flag = flag

    def check_flag(self):
        return self.flag


class Ride:
    def __init__(self, passengers_no, min_year):
        
        self.passengers = passengers_no
        self.min_year = min_year

    def suggest_vehicles(self, vehicles):
        suitable_vehicles = []
        for vehicle in vehicles:
            if vehicle.check_flag() and vehicle.capacity >= self.passengers and vehicle.year >= self.min_year:
                suitable_vehicles.append(vehicle)
        return suitable_vehicles



vehicles = []
for i in range(1):
    vehicle = Vehicle()
    print("Registaration of vehicle :", i+1)

    try:
        vehicle_type = input("What is the type of vehicle (SUV - Minivan - Sedan - Hatchback -Van)? ").lower()
    except ValueError as e:
        print("Error:", e)
        sys.exit(1)
    try:
        vehicle_capacity = int(input("What is the vehicle capacity for vehicle "+ str(i+1) +" ?"))
    except ValueError as e:
        print("Error:", e)
        sys.exit(1)
    try:  
        vehicle_year = int(input("What is the year of manufacture for vehicle "+ str(i+1) +" ?"))
    except ValueError as e:
        print("Error:", e)
        sys.exit(1)
    
    print("Vehicle ", i+1 ," has been registered")

    vehicle.set_vehicleInfo(vehicle_type, vehicle_capacity, vehicle_year)
    try:
        flag = input("Is vehicle " + str(i+1) + " available (True or False)? ").lower()
    except ValueError as e:
        print("Error:", e)
        sys.exit(1)
    if flag == "true":
        vehicle.set_flag(True)
    else:
        vehicle.set_flag(False)
    vehicles.append(vehicle)

print("Enter the information of the ride")
try:
    passenger_no = int(input("Enter the number of passenger: "))
except ValueError as e:
    print("Error:", e)
    sys.exit(1)

try:
    min_year = int(input("Enter the minimum manufacturing year of the vehicle: "))
except ValueError as e:
    print("Error:", e)
    sys.exit(1)

ride = Ride(passenger_no, min_year)
suitable_vehicles = ride.suggest_vehicles(vehicles)

print("The suggested vehicle(s) for you are:")
for vehicle in suitable_vehicles:
    print("Enter the minimum manufacturing year of the vehicle: 2016")
    print("Vehicle type:",vehicle.type.upper()," - year:",vehicle.year)
   