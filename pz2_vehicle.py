class Vehicle: 
    def __init__(self, make, model, year):
         self.__make = make
         self.__model = model
         self.__year = year
         self.__engine_started = False

    def start_engine(self):
         self.__engine_started = True
         print("Egine started")

    def stop_engine(self):
         self.__engine_started = False
         print("Engine stopped")

class Car(Vehicle):
    def __init__(self, make, model, year, num_doors, num_passangers):
        super().__init__(make, model, year)
        self.__num_doors = num_doors
        self.__num_passengers = num_passangers

    def drive(self):
        print("Car driving")
        
    def park(self):
        print("Car is parked")

class Truck(Vehicle):
    def __init__(self, make, model, year, max_load_capacity):
        super().__init__(make, model, year)
        self.__max_load_capacity = max_load_capacity

    def load_cargo(self):
        print("Truck is loaded")

    def unload_cargo(self):
        print("Truck is unloaded")

        

v1 = Vehicle("Car", "Light", 2015)
v1.start_engine()
v1.stop_engine()
v2 = Car("BMW", "M5", 2018, 4, 5)
v2.start_engine()
v2.drive()
v2.park()
v2.stop_engine()
v3 = Truck("Merin", "Gruzak", 2015, 3000)
v3.start_engine()
v3.load_cargo()
v3.unload_cargo()
v3.stop_engine()
