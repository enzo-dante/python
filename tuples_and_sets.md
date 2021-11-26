# tuples

> a tuple is an immutable (cannot be changed) ordered collection or grouping of items

__you cannot add or remove values from a tuple once it is set__

numbers = (1,2,3,4)

3 in numbers # True

numbers[0] = "test" # TypeError

__tuples are faster and safer than lists since they are not expected to change__

months = ("January", "February")

__tuples are valid keys in a dictionary, unlike lists which cannot be used as keys in a dictionary__ 

locations = {
    (35.1, 39.6): "Tokyo Office",
    (40.7, 74.0): "New York Office"
}

locations[(35.1, 39.6)] # 'Tokyo Office'

> accessing values in a tuple

months = ("January", "February")

months[-1] # 'February'

> dictionary.item() returns a tuple

test = {
    1: "a",
    2: "b"
}

test.items() # dict_items([(1, 'a'), (2, 'b')])

> iterating over tuples

months = ("January", "February")

for month in months:
    print(month)

i = len(months) - 1

while(i >= 0):
    print(months[i])
    i--

# tuple methods

> tuple.count() = returns the number of times a value appears in a tuple

x = (1,3,2,3,4)
x.count(3) # 2
x.count(4) # 1

> tuple.index() = returns the index at which a value is found in a tuple

a = (1,3,2,3,4)
a.index(1) # 0
a.index(5) # ValueError
a.index(3) # 1 -- since the first matching index is returned

# nested tuples

nums = (1,2, ("a", "b"), 4)

# tuple slicing

nums = (1,2, ("a", "b"), 4)
nums[0:] # (1,2, ("a", "b"), 4)

nums[0:2] # (1,2)

nums[1::2] # (2,4)

# Sets

> sets are collections that do not have order and contain unique non-duplicate values that cannot be accessed by an index

set_1 = set({1,2,3,3, 4,5}) # {1,2,3,4,5}

set_2 = {1,4,5, "test", 3.4}

__sets can be useful if you need to keep track of a collection of elements, but do not care about ordering, keys-value pairs, or having duplicates__

4 in set_2 # True

8 in set_1 # False

> accessing all values in a set

numbers = {1,2,3,4}

for n in numbers:
    print(n)

> get unique values via set() and convert to a list

cities = ["LA", "Tokyo", "LA"]

print(list(set(cities))) # {"LA", "Tokyo"}

> get number of unique values via set

print(len(set(cities)))

# set methods

> set.add(value) = adds a value to set if the set doesn't already contain the provided value

set_1 = {1,2,3}

set_1.add(4)

s # {1,2,3,4}

> set.discard(value) = remove a value from a set with no error on attempt to remove non-existent value in the set
>
> set.remove(value) = remove a value from a set and will throw error on attempt to remove non-existent value in the set

set_1 = {1,2,3}

set_1.remove(2)
set_1 # {1,3}

> set.copy() = makes a copy of the set that is identical in values (==), but not identical in memory reference (IS)

set_1 = {1,2,3}
copy_set = set_1.copy()

copy_set # {1,2,3}

set_1 == copy_set # True because identical values
set_1 is copy_set # False because they hold diffence places in memory

> set.clear() = removes all content from the set

s = set({7, 8.1, "Test"})
s.clear()

s # set()

# set math: union and intersection

math_students = {"M", "H", "P", "J", "A"}
biology_students = {"J", "M", "C", "M2", "O", "J"}

> set_1 | set_2 = set UNION of unique values from 2 or more sets

math_students | biology_students # {'C', 'A', 'J', 'M2', 'H', 'O', 'P', 'M'}

> set_1 & set_2 = set INTERSECTION of unique values that are in all provided sets 

math_students & biology_students # {'J', 'M'}

# set comprehension

__rapidly create sets with shortcut notation just like dictionary comprehension and list comprehension respectively__

> set comprhension syntax is similar to dictionary comprehension BUT WITHOUT the key-value notation
>
> {<value_logic> for <value> in <length>}

__set comprehension creates sets that have no specific order__

{x**2 for x in range(10)} # {0,1,64,4,36,9,16,49,81,25}

> if you add the key-colon the syntax, a dictionary will be created, but leaving out the key-colon syntax a set will be created

{x**2 for x in range(10)} # {0,1,64,4,36,9,16,49,81,25}

{x:x**2 for x in range(10)} # {0:0,1:1,2:4,3:9,4:16, 5:25, 6:36, 7:49, 8:64, 9:81}

> set comprehension can also work with strings

{char.upper() for char in "hello"} # {'L', 'O', 'H', 'E'}

> function that returns True or False if that string contains all vowels using set comprehension that uses conditional logic

__length of resulting set produced from processed string will return True or False depending on if it contained all vowels 'aeiou' which has a length of 5__

def are_all_vowels_in_string(string):
    return len({char for char in string if char in "aeiou"}) == 5

string_1 = "hello"
string_2 = "sequoia"

are_all_vowels_in_string(string_1) # False
are_all_vowels_in_string(string_2) # True