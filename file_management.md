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

# R+ = read and write based on cursor position in PRE-EXISTING file

> r+ (read & write default at beginning) REQUIRES a pre-existing and you still have to open() a file

> SUPERIOR write option:

__add -r+ flag to append in open()__

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
