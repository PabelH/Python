from pickle import *


class Vehicle:

    def __init__(self, color, doors):
        self.color = color
        self.doors = doors

    def __str__(self):
        return self.color + " " + self.doors


chevy = Vehicle("Black", "5")
print(chevy)

file = open('vehicle_object', 'w+b')

dump(chevy, file)

file.seek(0)
new_chevy = load(file)

print(new_chevy)
file.close()
