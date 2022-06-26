# CSV module reader

> reader - lets you iterate over rows of the CSV as lists

from csv import reader
with open("fighters.csv") as file:
    csv_reader = reader(file)

__the csv file will start with the header row, so use next() to start on row with values__
    next(csv_reader)

    for row in csv_reader:
__accessing values requires using indecies__
        print(f"{fighter[0]} is from {fighter[1]}")

        # each row in a list!
        print(row)

__if you try and call csv_reader again, it will be at the end of the CSV and cannot call next()__
    for row in csv_reader:
        print(f"{fighter[0]} is from {fighter[1]}")

        # each row in a list!
        print(row)

> reader - iterating with a CSV converted list

from csv import reader
with open("fighters.csv") as file:
    csv_reader = reader(file)
    data = list(csv_reader)
    print(data)

> DictReader - lets you iterate over rows of the CSV as OrderedDicts

from csv import DictReader as dread

with open("fighters.csv") as file:
    csv_reader = dread(file)

    for row in csv_reader:
        # each row is an OrderedDict (a dictionary with an order)

__each row has the headers interspersed as keys__
        print(row["Name"])

> readers allow for specifying a delimiter kwarg in case your data isn't separated by commas

from csv import reader

with open("fighters.csv") as file:
    csv_reader = reader(file, delimiter="|")
    for row in csv_reader:
        # each row is a list!
        print(row)

# writing CSV files (LISTS)

> the writer creates a writer_object fro writing a csv

> writer.py

from csv import writer

__writerow(["a", "b"]) will add a row to a csv_file__

with open("cats.csv", "w") as file:
    csv_writer = writer(file)

__to add headers, simply write another row with writer_object__
    csv_writer.writerow(["Name", "Age"]) # headers

__to add data, simply write another row with writer_object__
    csv_writer.writerow(["Blue", 3])
    csv_writer.writerow(["Unnamed Kitty", 1])

__to run, execute: python3 writer.py__

> update an existing file using reader and writer

> writer.py

from csv import reader, writer

with open("fighters.csv") as file:

__reader() is the CSV method that lets you read CSV rows into memory as lists__

    csv_reader = reader(file)

    # use list comprehension to build uppercase data, csv = nested list
    fighters = [[s.upper() for s in row] for row in csv_reader]

    for row in fighters:
        print(row)

with open("screaming_fighters", "w") as file:
    csv_writer = writer(file)

__loop through list (that includes headers) and writerow(["a", "b"]) will add a row to a csv_file__

    for fighter in fighters:
        csv_writer.writerow(fighter)

# writing CSV files (DICTIONARIES)

> example 1

__DictWriter - creates a writer object for writing using dictionaries__

from csv import DictWriter

with open("example.csv", "w") as file:
    headers = ["Character", "Move"]
__fieldnames - kwarg for the DictWriter specifying headers__
    csv_writer = DictWriter(file, fieldnames=headers)
__writeheader - method on a writer to write header row__
    csv_writer.writeheader()
__writerow - method ona writer to write a row based on a dictionary__
    csv_writer.writerow({
__headers & respective insert data don't have to be in a specific order__
        "Character":"Ryu",
        "Move": "Hadouken"
    })

> example 2

from csv import DictWriter

with open("cats.csv", "w") as file:
    headers = ["Name", "Breed", "Age"]
    csv_writer = DictWriter(file, filename=headers)
    csv_writer.writeheader()
    csv_writer.writerow({
        "Age": 20
        "Breed": "Orange",
        "Name": "Garfield",
    })

> example 3: using DictReader & DictWriter with target updating

from csv import DictReader, DictWriter

def cm_to_in(cm):
    return float(cm)*0.393701

with open("fighters.csv") as file:
    csv_reader = DictReader(file)
    fighters = list(csv_reader)

with open("inches_fighters.csv", "w") as file:
    headers = ["Name","Country","Height"]
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()

__loop through each row and set height with defined function__

    for f in fighters:
        csv_writer.writerow({
            "Name": f["Name"],
            "Country": f["Country"],
            "Height": cm_to_in(
                    f["Height (in cm)"]
                )
        })

# pickle: convert python into unreadable data for storage

> pickle external module will serialize into a byte stream -- akin to putting it into a jar for storage and can be deserialized back into a python object on command

> example 1:

import pickle

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __repr__(self):
        return f"{self.name} is a {self.species}"

    def make_sound(self, sound):
        print(f"this animal says {sound}")

class Cat(Animal):

    def __init__(self, name, breed, toy):
        super().__init__(name, species="Cat")
        self.breed = breed
        self.toy = toy

blue = Cat("Blue", "Scottish Fold", "String")

__wb = write binary for serialized byte stream__

with open("pets.pickle", "wb")as file:

__pickle.dump() will pickle the python__

    pickle.dump(blue, file)

__when the data uses tuples and is pickled, it will be returned in that order__

blue = Cat("Blue", "Scottish Fold", "String")

with open("pets.pickle", "wb")as file:

__pickle.dump() can pickle tuple objects__

    pickle.dump(("Blue", "Rusty"), file)

__rb = read binary for serialized byte stream to load back into python__

with open("pets.pickle", "rb") as file:
    zombie_blue, zombie_rusty = pickle.load(file)
    print(zombie_blue)
    print(zombie_blue.play())

> unpickling: deserialize the byte data back into a python object

with open("pets.pickle", "rb") as file:

__pickle.load() will deserialize byte data back into a python__

    zombie_blue = pickle.load(file)
    print(zombie_blue)
    print(zombie_blue.play())

# json pickling

> jsonpickle is an external module that serializes and deserializes python objects to and from json

__pip install jsonpickle in the terminal__

python3 -m pip install jsonpickle

import jsonpickle

class Cat:

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

c = Cat("Charlie", "Tabby")

> serialize python obj with jsonpickle encode()

__open and write the content of the file first__

with open("cat.json", "w") as file:
    serialized_c = jsonpickle.encode(c)
    file.write(serialized_c)

> deserialize python obj with jsonpickle decode()

with open("cat.json", "r") as file:

__open and read the content of the file first__

    contents = file.read()
    deserialized_c = jsonpickle.decode(contents)
    print(deserialized_c)

> json.dumps() converts a python object as a str of json

import json

j = json.dumps(['foo', {'bar': ('bas', None, 1.0, 2)}])

print(j)