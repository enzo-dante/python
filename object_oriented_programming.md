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

> inheritance is the ability to define a class which inherits from another class, the parent/base class

__in python, inheritance works by assessing the parent class as an argument to the definition of a child class__

class Animal:

    def make_sound(self, sound):
        print(sound)

    cool = True

class Cat(Animal):
    pass

gandalf = Cat()
gandalf.make_sound("meow") # meow
gandalf.cool # True

__isinstance(variable, data_type) will verify class hierarchy__

isinstance(gandalf, Cat) # True
isinstance(gandalf, Animal) # True
isinstance(gandalf, object) # True

# @property

> use @property decorator to define properties that work as setters and getters

__use @property decorator to set up a setter and getter age and fullname properties for human class__

class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self._age = age

    @property # getter
    def age(self):
        return self._age

    @age.setter # setter are helpful for value validation
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            raise ValueError("age cannot be negative")

    @property
    def full_name(self):
        return f"{self.first} {self.last}"

    @full_name.setter
    def full_name(self, value):
        if value:
            self.first, self.last = value.strip().split(" ")
        else:
            raise ValueError("full name must be a valid str")

enzo = Human("Enzo", "Dante", 49)

__when getting properties, you don't need paranthesis even though its a method__

print(enzo.age) # 49

> the @property is interfacing with the "private" variable self._age -- remember that python technically doesn't manage public and private access

enzo.age = 21
print(enzo.age) # 21
    print(enzo.full_name) # Enzo Dante

# super()

> avoid duplication by using inheritance with super()

class Animal:

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __repr__(self):
        return f"{self.name} is a {self.species}"

    def make_sound(self, sound):
        print(f"this animal says {sound}")

class Cat(Animal):

    def __init__(self, name, species, breed, toy):

__superior option: use super() for inheritance which doesn't require self in definition and can use default parameters__
        super().__init__(name, species="Cat")

__inferior option: use parent class init with child class init__
        Animal.__init__(self, name, species)

        self.breed = breed
        self.toy = toy

    def play(self):
        return f"{self.name} plays with {self.toy}"

blue = Cat("Blue", "Scottish Fold", "String")
print(blue.play()) # Blue plays with String

# multiple inheritance

> multiple inheritance generally makes tracing Method Resolution Order (MRO) confusing between classes
>
> the application of multiple inheritance is rare in production but helps with understanding how python works

class Aquatic:
    def __init__(self, name):
        print("Aquatic init")
        self.name = name

    def swim(self):
        return f"{self.name} is swimming"

    def greet(self):
        return f"I am {self.name} of the sea!"

class Ambulatory:
    def __init__(self, name):
        print("Ambulatory init")
        self.name = name

    def walk(self):
        return f"{self.name} is walking"

    def greet(self):
        return f"I am {self.name} of the land!"

class Penguin(Ambulatory, Aquatic):
    # since Ambulatory is 1st class argument, it takes precedence in inheritance order

    def __init__(self, name):
        print("Penguin init")

        # when using multiple inheritance, its better to be explicit with the parent class
        Ambulatory.__init__(self, name=name)
        Aquatic.__init__(self, name=name)

        # super().__init__(name=name)

jaws = Aquatic("Jaws")
lassie = Ambulatory("Lassie")
captain_hook = Penguin("Captain Hook")

print(isinstance(captain_hook, Penguin)) # True
print(isinstance(captain_hook, Aquatic)) # True
print(isinstance(captain_hook, Ambulatory)) # True

print(captain_hook.swim())
print(captain_hook.walk())

    # .greet() inherits from Ambulatory not Aquatic class due to class argument inheritance order
print(captain_hook.greet())

> method resolution order (MRO) is the order in which Python will look for methods on instances of that class aka a hierarchy, which is how super() chooses it's order if there methods with the same name

class A:
    def do_something(self):
        print("Method Defined In: A")

class B(A):
    def do_something(self):
        print("Method Defined In: B")

class C(C):
    def do_something(self):
        print("Method Defined In: C")

class D(B,C):
    def do_something(self):
        print("Method Defined In: D")

thing = D()
thing.do_something()

__ambiguous inheritance between classes, but order is D, B, C, A, Object__

__help(D) will print out mro for class D__

help(D)

>    A
>   / \
>  B   C
>   \ /
>    D

# polymorphism

> a key principle in OOP is the idea of polymorphism - an object can take on many (poly) forms (morph)

__application 1: the same method works in a similar way for different classes__

> "method overriding" is a common example where a parent method is overridden by the child method of the same name

class Animal:
    def speak(self):
        raise NotImplementError("Subclass needs to implement this method")

class Dog(Animal):
    def speak(self):
        return "woof"

class Cat(Animal):
    def speak(self):
        return "meow"

class Human(Animal):
    pass

Cat.speak() # 'meow'
Dog.speak() # 'woof'
Human.speak() 'Subclass needs to implement this method'

__application 2: the same operation works for different kinds of objects__

sample_list = [1,2,3]
sample_tuple = (1,2,3)
sample_string = "awesome"

len(sample_list)
len(sample_tuple)
len(sample_string)

# built-in magic dunder methods can be overridden

> __add__(self, var) = "+" operator

8 + 2 = 10
8 + "2" = 82

> __len__(self, var) = len()

test = [1,2,3]
len(test) # 3

__the below Human class demonstrates how a lot of built-in dunder methods can be overridden manually__

from copy import copy

class Human:

    def __init__(self, first, last,age):
        self.first = first
        self.last = last
        self.age = age

    def __repr__(self):
        return f"Human named {self.first} {self.last} with age {self.age}"

    def __len__(self):
        return self.age

    def __add__(self, other):
        if isinstance(other, Human):
            return Human(first="newborn", last=self.last, age=0)
        
        raise TypeError("You cannot add that!)

    def __mul__(self, other):
        if isinstance(other, int):
            return [copy(self) for i in range(other)]
        
        raise TypeError("You cannot multiply")

j = Human("Jenny", "Owen", 47)
k = Human("Kenny", "Richards", 91)
print(j)

print(j + k)
print(len(j)) # 47 instead of a TypeError

print(j * 2) # "YOU ARE MULTIPLYING HUMANS"

> overriding a dictionary

