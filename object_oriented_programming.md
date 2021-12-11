# OOP = object oriented programming

> a method of programming (not specific to python) that attempts to model a process or thing in the world to encapsulate (logical hierarchial groupings of private and public attributes & methods) using classes or objects for abstraction

__class = a capitalized single name blueprint for objects, that utilizes abstraction (expose only relevant methods aka object functions and attributes for public interface)__

class Vehicle:
    pass 

    def add_gas(a):
        return a + 1 

__instance = objects that are constructed from a class blueprint that contain their class' methods and properties__

car = Vehicle()

> it is common to place an underscore in front a variable to denote to other develops that a variable is private (python doesn't explicitly restrict public and private access though)
>

example: _cards

