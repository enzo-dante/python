# OOP = object oriented programming

> a method of programming (not specific to python) that attempts to model a process or thing in the world to encapsulate (logical hierarchial groupings of private and public attributes & methods) using classes or objects for abstraction

__class = a capitalized single name blueprint for objects, that utilizes abstraction (expose only relevant methods aka object functions and attributes for public interface)__

class Vehicle:

> class attributes are defined once and placed at the top of the class object and can be used for validation
        acive_users = 0

> the __init__ dunder method (instantiate with double underscores) gets called every time you create an instance of the class
>
> the self keyword refers to the current instance of the class(which could technically be called anything, but convential to use self)

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.mantra = "need for speed"

__every time a Vehicle instance is created, active_users class variable is added 1__
        Vehicle.active_users += 1

__it is common to place an underscore (_) in front a variable to denote to other developers that a variable is private (python doesn't explicitly restrict public and private access though)__

        self._secret = "python technically doesn't public/private access"

__name mangling = place double underscores in front of an attribute (__)
        self.__msg = "this message cannot be inherited by other classes due to name mangling and is unique to this class"

__classes can have methods (which are object functions) associated with them and the class attributes can be accessed via the self keyword__

    def add_gas(self, a):
        return f"{a} gallons of gas was added to {self.model}"

    def get_model_initials(self):
        return f"{self.model[0]}{self.year[2:]}"

    def is_old(self):
        return self.year >= 65

    def change_mantra(self):
        self.mantra = f"self.mantra[:4] you in my life"
        return self.mantra

    def power_off(self):
        Vehicle.power_off -= 1
        return f"{self.model} has powered down"

__instance = objects that are constructed from a class blueprint that contain their class' methods and properties__

my_car = Vehicle("hyundai", "elantra", 2014)
your_car = Vehicle("honda", "civic", 2006)

__instance.{attribute_name} = access specific attributes on an instance__

print(my_car.year) # 2014
print(your_car.year) # 2006
print(your_car.get_model_initials()) # 2006
print(your_car.change_mantra()) # 2006

print(Vehicle.active_users)
print(my_car.power_off())
print(Vehicle.active_users)

# class attributes

> class attributes/variables are defined once and placed at the top of the class object and can be used for validation

class Pet:

    allowed_species = ["cat", "dog", "fish", "rat"]

    def __init__(self, name, species):
        if species not in Pet.allowed_species:
            raise ValueError(f"You cannot have a {species} pet")
        self.name = name
        self.species = species

    def set_species(self, species):
        if species not in Pet.allowed_species:
            raise ValueError(f"You cannot have a {species} pet")
        self.species = species

cat = Pet("blue", "cat")
dog = Pet("stone", "dog")

# class methods

> class methods are methods (that use the @classmethod decorator) that are only concerned with the class itself and not the instances
>
> rare compared to instance methods

class Person:

    thought = "I am alive"

    def __init__(self, name):
        self.name = name

__conventional to use cls (class and not instance of the class) for class method arguments__

    @classmethod
    def display_thought(cls):
        return cls.thought

print(Person.display_thought())

> the most common use case for class method is to handle csv (comma-seperated-values)

dict.fromkeys(["name", "age"], "unknown") # {"name": "unknown", "age": "unknown"}

class User:

    active_users = 0

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1

> __repr__ is a dunder method that allows for formatting a class into a string representation

    def __repr__(self):
        return f"{self.first} is {self.age}"

    @classmethod
    def from_string(cls, data_string):
        first, last, age = data_string.split(",")
        return cls(first, last, int(age))

    def get_full_name(self):
        return f"{self.first} {self.last}"

tom = User.from_string("Tom,Jones,89")
print(tom.first)
print(tom.get_full_name()) # "Tom Jones"

> __repr__ displaying the respective dunder method that shows a string instead of the class object

kate = User("kate", "vernon", 18)
print(str(kate)) # 'kate is 18'

# inheritance