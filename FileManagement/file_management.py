"""
    ? MODES 

        modes for opening files

        * r 

            read a file (no writing) - this is the default behavior

        * w 

            write a file (previous content will be removed)

            can write to a pre-existing or create a new file

        * a 

            append to a file (previous content will NOT be removed)

            can write to a pre-existing or create a new file

            append does not allow for cursor control

            only adds to end

        * r+ 

            read and write to a file (writing based on cursor)

            requires a pre-existing file

            r+ by default adds to beginning/seek(0)
"""

# ! open(file_name) + opened_file.read()

#   read files in python
#       after reading a file, you need return cursor back to the start of the file

#       default -r flag is included in open(file_name)
"""
* story.txt

    "this story is really short
    This is awkward"

* read_file.py
"""

my_file = open("story.txt")
my_file.read()

# ? for documentation, refer to:

file_obj = "read_file.py"
help(file_obj)

"""
! file cursor movement

    after reading a file, use seek() to set cursor to specific position

    after reading a file, you need return cursor back to the start of the file
"""

# ! file.seek(0)

#   bring file back to beginning

my_file.seek(0) # 'this story is really short\nThis is awkward'

# ! file.readline()

#   read the first line

my_file.readline() # 'this story is really short'

# ! file.readlines()

#   preserve lines and places them in a list__
my_file.readlines() # ['this story is really short', 'This is awkward']

# ! file_object.close()

#   ALWAYS close a file after use to free up computational resources

#   if closed, the file_object cannot be read again until re-opened

my_file = open("story.txt")
my_file.read()

my_file.close()
my_file.closed # True
