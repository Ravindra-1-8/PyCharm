# Passing Arguments to "init" Constructor.
class Car:
    wheel = 4

    def __init__(self,name,speed):
        self.name = name
        self.speed = speed

    def display(self):
        print(self.wheel)
        print(self.name)
        print(self.speed)

c1 = Car("Bugatti","300mph")
c1.display()

print("\n")

c2 = Car("BMW","200mph")
c2.display()