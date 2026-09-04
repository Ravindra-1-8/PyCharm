#__init__ is a special method(constructor).
#__init__ runs automatically when an object is created.
#self stores data inside the object.

class Car:
    name = "Pagani"
    color = "SkyBlue"

    def __init__(self):   # By using __init__ constructor there is no need to class the function separately.
        print(self.name,self.color)
        print("300mph")

    def speed(self):
        print("Speed Noted")

c1 = Car() # c1 is an object.
c1.speed() 