# Creating functions inside class.

# Self always represents object.
# "self" connects object to class.
# Whenever we declare "functions", inside class we need to use keyword "self" for accessing.

class Student:
    def studentdetails(self,name,age):
        print(name,age)

s1 = Student() # Creating of objects.
print(s1)
s1.studentdetails("Lucky",44)

class Car:
    name = "Bugatti"
    color = "Red"

    def speed(self):
        print(self.name,self.color) # Accessing variables inside the function.
        print("300mph")

c1 = Car()# object creation.
c1.speed() # calling the function.
