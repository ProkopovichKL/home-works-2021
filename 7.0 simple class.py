class Bike:
    def __init__(self, manuf_model, bike_type, frame, gear, seats_number, wheels_number, brakes, speed):
        if gear not in range(1, 35) or seats_number not in range(1, 6) or wheels_number not in range(1, 6) or speed not in range(1, 234):
            raise ValueError("Such a set of bike characteristics is hardly possible. Check and try again")
        self.__manufacturer_model  = manuf_model
        self.__bike_type = bike_type
        self.__frame_material = frame
        self.__gear = gear
        self.__seats_number = seats_number
        self.__wheels_number = wheels_number
        self.__brakes = brakes
        self.__max_speed = speed
        
    def presentation(self):
        print("\nBike model -", self.__manufacturer_model)
        print("Bike type -", self.__bike_type)
        print("Bike frame material -", self.__frame_material)
        print("Number of gears -", self.__gear)
        print("Number of seats -", self.__seats_number)
        print("Number of wheels -", self.__wheels_number)
        print("Brake type -", self.__brakes)
        print("Maximum speed (km/h) -", self.__max_speed)

    def get_model(self):
        print("Bike model -", end = ' ')
        return self.__manufacturer_model
    
    def get_type(self):
        print("Bike type -", end = ' ') 
        return self.__bike_type
    
    def get_frame(self):
        print("Bike frame material -", end = ' ')
        return self.__frame_material
    
    def get_gear(self):
        print("Number of gears -", end = ' ')
        return self.__gear

    def get_seats_number(self):
        print("Number of seats -", end = ' ')
        return self.__seats_number

    def get_wheels_number(self):
        print("Number of wheels -", end = ' ')
        return self.__wheels_number

    def get_brakes(self):
        print("Brake type -", end = ' ')
        return self.__brakes
    
    def get_speed(self):
        print("Maximum speed (km/h) -", end = ' ')
        return self.__max_speed

    def set_model(self, model):
        self.__manufacturer_model = model

    def set_type(self, bike_type):
        self.__bike_type = bike_type

    def set_frame(self, frame):
        self.__frame_material = frame

    def set_gear(self, gear):
        if gear in range(1, 35):
            self.__gear = gear
        else:
            print("Such a number of gears is hardly possible. Check and try again")
        
    def set_seats_number(self, seats_number):
        if seats_number in range(1, 6):
            self.__seats_number = seats_number
        else:
            print("Such a number of seats is hardly possible. Check and try again")

    def set_wheels_number(self, wheels_number):
        if wheels_number in range(1, 6):
            self.__wheels_number = wheels_number
        else:
            print("Such a number of wheels is hardly possible. Check and try again")
    
    def set_brakes(self, brakes):
        self.__brakes = brakes

    def set_speed(self, speed):
        if speed in range(1, 234):
            self.__max_speed = speed
        else:
            print("Such a number of speed is hardly possible. Check and try again")

    def move(self):
        print(self.__manufacturer_model, "is moving now and can go", self.__max_speed, "km/h!")

    def stop(self):
        print("You whant STOP! Ok,", self.__manufacturer_model, "is stoping now... He stopped at last!")
    
    x_model = property(get_model, set_model)
    x_type = property(get_type, set_type)
    x_frame = property(get_frame, set_frame)
    x_gear = property(get_gear, set_gear)
    x_seats_number = property(get_seats_number, set_seats_number)
    x_wheels_number = property(get_wheels_number, set_wheels_number)
    x_brakes = property(get_brakes, set_brakes)
    x_maks_speed = property(get_speed, set_speed)

bike1 = Bike("Aist", "highway", "metal", 1, 1, 2, "drum", 50)
bike1.presentation()
print(bike1.get_model())
bike1.x_model = "Stels"
print(bike1.x_model)
bike1.set_speed(100)
bike1.x_wheels_number = 5
bike1.x_brakes = "disc"
bike1.presentation()
bike1.move()
bike1.stop()




