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

* ex) story.txt

    "this story is really short
    This is awkward"
"""

story_file = "story.txt"
new_file = "newly_created.txt"

"""
    ? SUPERIOR READING FILES: Block statements 

! with open(file_name) as file:

    * with open(file_name) =  file.__exit__() / file.close() automatically called after use

    default -r flag is included in with open(file_name)

* ex) read_file.py
"""

with open(story_file) as file:
    data = file.read()

print(file.closed) # True

"""
! WRITE ("w")

    overriding existing content in target file

    to write to a pre-existing or non-existing (will be created) files
        * still requires open() a file
"""

with open(story_file, "w") as file:
    file.write("Writing files is great\n")
    file.write("Closing now, bye!\n")

"""

! APPEND ("a")

    overriding existing content in target file

    to append (always to end) to a pre-existing or non-existing (will be created) files

        generally, include \n for new line at end w/ APPEND flag

        * still requires open() a file

    ? APPEND flag DOES NOT remove/override original content
"""

with open(new_file, "a") as file:
    file.write("Writing files is great\n")
    file.write("Closing now, bye!\n")

"""

! READ & WRITE ("r+") 

    read and write based on cursor position in PRE-EXISTING file

    ? r+ (read & write default at beginning) REQUIRES a pre-existing 
        * still requires open() a file

    ! r+ flag will REMOVE/override original content cursor position already has content
"""

search_word = "awkward"
replacement_word = "super"

with open(story_file, "r+") as file:
    # read file content and store to data variable
    data = file.read()

    # cursor seek beginning of file to prepare for write
    file.seek(0)

    # replace the searched_word with replacement_word
    updated_data = data.replace(search_word, replacement_word)

    # write the new content over the old content
    file.write(updated_data)

    # Truncate() method truncate the file’s size (optional flag) 
    # The current file position is not changed & the size defaults to the current position. 
    file.truncate()

# ! TARGET WRITING r+

#   use file_object.seek(position) with "r+" for target writing

with open(story_file, "r+") as file:
    file.write("The beginning by default\n")
    file.seek(10)
    file.write("went to position 10\n")

# ! copy

#   copy contents from one file to another

copy(story_file, new_file)

"""
    ? INFERIOR READING FILES: open() statements 

! open(file_name) + opened_file.read()

    read files in python

        after reading a file, you need return cursor back to the start of the file

    default -r flag is included in open(file_name)

* ex) read_file.py
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
