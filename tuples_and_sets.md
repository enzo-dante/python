# tuples

> a tuple is an immutable (cannot be changed) ordered collection or grouping of items

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

# accessing values in a tuple

months = ("January", "February")

months[-1] # 'February'

# dictionary.item() returns a tuple

test = {
    1: "a",
    2: "b"
}

test.items() # dict_items([(1, 'a'), (2, 'b')])

# iterating over tuples

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
