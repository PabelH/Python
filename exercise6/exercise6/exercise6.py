
class Vehicle():

    def __init__(self, color, wheels, doors):
        self.color = color
        self.wheels = wheels
        self.doors = doors

    def __str__(self):
        return "Color {}, {} wheels".format( self.color, self.wheels, self.doors )

class Car(Vehicle):

    def __init__(self, color, wheels, doors, speed, cylinderCap):
        self.color = color
        self.wheels = wheels
        self.doors = doors
        self.speed = speed
        self.cylinderCap = cylinderCap

    def __str__(self):
        return "color {}, {} km/h, {} wheels, {} doors, {} cc".format( self.color, self.speed, self.wheels, self.doors, self.cylinderCap )


car = Car("black", 4, 5, 180, 1320)
print(car)