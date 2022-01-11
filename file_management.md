# modes for opening files

r - read a file (no writing) - this is the default behavior

w - write a file (previous content will be removed)
    * can write to a pre-existing or create a new file

a - append to a file (previous content will NOT be removed)
    * can write to a pre-existing or create a new file
    * append does not allow for cursor control
    * only adds to end

r+ - read and write to a file (writing based on cursor)
    * requires a pre-existing file
    * r+ by default adds to beginning/seek(0)

# READING FILES option 1: open()/read()

> use open(file_name) & opened_file.read() to read files in python

ex:

> story.txt

'this story is really short
This is awkward'

> reading_files.py

my_file = open("story.txt")
my_file.read()

__after reading a file, you need return cursor back to the start of the file__

# file cursor movement

> after reading a file, use seek() to set cursor to specific position
>
> for documentation, refer to:
>
>       help(file_object)

__default -r flag is included in open(file_name)__

my_file = open("story.txt")
my_file.read() # 'this story is really short
This is awkward'

my_file.read() # ''

__file.seek(0) = bring file back to beginning__

my_file.seek(0) # 'this story is really short\nThis is awkward'

__file.readline() = read the first line__

my_file.readline() # 'this story is really short'

my_file.readline() # 'This is awkward'

__file.readlines() = preserve lines and places them in a list__

my_file.readlines() # 'this story is really short
This is awkward'

> file_object.close() = ALWAYS close a file after use to free up computational resources

my_file = open("story.txt")
my_file.read()

my_file.close()
my_file.closed # True

__if closed, the file_object cannot be read again until re-opened__

my_file = open("story.txt")
my_file.read()

my_file.close()

# READING FILES option 2: with Block statements

__default -r flag is included in open(file_name)__

with open("story.txt") as file:
    data = file.read()

__using with automatically closes a file__

    # file.__exit__()/file.close() is automatically called

print(file.closed) # True
print(data) # 'This story is really short'

# WRITE ("w") = overriding existing content in target file

> to write to a pre-existing or non-existing (will be created) files, you still have to open() a file

> SUPERIOR write option:

__add -w flag to write in open()__

__-w flag overrides orginal content__

with open("newly_created.txt", "w") as file:
    file.write("Writing files is great\n")
    file.write("Here is another line of text\n")
    file.write("Closing now, goodbye!\n")

> INFERIOR write option: need to manually close

file = open("newly_created.txt", "w")

file.write("Writing files is great\n")
file.close()
file.closed # True

__to test write, go into terminal run: python3 file_name__

# APPEND ("a") = overriding existing content in target file

> to append (always to end) to a pre-existing or non-existing (will be created) files, you still have to open() a file

> SUPERIOR write option:

__add -a flag to append in open()__

__-a flag DOES NOT remove/override orginal content__

__generally, when using -a flag, include \n for new line at end__

with open("newly_created.txt", "a") as file:
    file.write("Writing files is great\n")
    file.write("Here is another line of text\n")
    file.write("Closing now, goodbye!\n")

> INFERIOR write option: need to manually close

file = open("newly_created.txt", "a")

file.write("Writing files is great\n")
file.close()
file.closed # True

__to test write, go into terminal run: python3 file_name__

# r+ = read and write based on cursor position in PRE-EXISTING file

> r+ (read & write default at beginning) REQUIRES a pre-existing and you still have to open() a file

> SUPERIOR write option:

__"r+" arg in open() = read and write in pre-existing file__

with open(file_name, "r+") as file:
    # read file content and store to data var
    data = file.read()
    # cursor seek beginning of file to prepare for write
    file.seek(0)
    # replace the searched_word with replacement_word
    updated_data = data.replace(search_word, replacement_word)
    # write the new content over the old content
    file.write(updated_data)
    # Truncate() method truncate the file’s size. If the optional size argument is present, the file is truncated to (at most) that size. The size defaults to the current position. The current file position is not changed.
    file.truncate()

__-r+ flag will remove/override orginal content cursor position already has content__

__use file_object.seek(position) with "r+" for target writing__

with open("temp.py", "r+") as file:
    file.write("using r+ = reading and writing\n")
    file.write("Here is another line of text\n")
    file.write("Closing now, goodbye!\n")

with open("temp.py", "r+") as file:
    file.write("The beginning by default")
    file.seek(10)
    file.write("Went to position 10")

__to test write, go into terminal run: python3 file_name__

# copy

> Copy should copy contents from one file to another.

copy('story.txt', 'story_copy.txt') # None

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

# pickling

> pickle external module will convert into a byte stream -- akin to putting it into a jar for storage

ex:

> pickiling is for dumping data & loading it quickly

__when the data is pickled, it will be unreadable to the human eye__

blue = Cat("Blue", "Scottish Fold", "String")

with open("pets.pickle", "wb")as file:
    pickle.dump(blue, file)

__when the data uses tuples and is pickled, it will be returned in that order__

blue = Cat("Blue", "Scottish Fold", "String")

with open("pets.pickle", "wb")as file:
    pickle.dump(("Blue", "Rusty"), file)

with open("pets.pickle", "rb") as file:
    zombie_blue, zombie_rusty = pickle.load(file)
    print(zombie_blue)
    print(zombie_blue.play())

> unpickiling

with open("pets.pickle", "rb") as file:
    zombie_blue = pickle.load(file)
    print(zombie_blue)
    print(zombie_blue.play())
