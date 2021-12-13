# OOP = object oriented programming

> a method of programming (not specific to python) that attempts to model a process or thing in the world to encapsulate (logical hierarchial groupings of private and public attributes & methods) using classes or objects for abstraction

__class = a capitalized single name blueprint for objects, that utilizes abstraction (expose only relevant methods aka object functions and attributes for public interface)__

class Vehicle:

> the __init__ dunder method (instantiate with double underscores) gets called every time you create an instance of the class
>
> the self keyword refers to the current instance of the class(which could technically be called anything, but convential to use self)

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

__it is common to place an underscore (_) in front a variable to denote to other developers that a variable is private (python doesn't explicitly restrict public and private access though)__

        self._secret = "python technically doesn't public/private access"

__name mangling = place double underscores in front of an attribute (__)
        self.__msg = "this message cannot be inherited by other classes due to name mangling and is unique to this class"

    def add_gas(self, a):
        return a + 1

__instance = objects that are constructed from a class blueprint that contain their class' methods and properties__

my_car = Vehicle("hyundai", "elantra", 2014)
your_car = Vehicle("honda", "civic", 2006)

__instance.{attribute_name} = access specific attributes on an instance__

print(my_car.year) # 2014
print(your_car.year) # 2006
