# dictionaries = key-value pairs

> keys describe data, values represent the data
>
> keys are almost always strings or numbers, but values can be anything

instructor = {
    "name": "Enzo",
    "owns_dog": False,
    "num_courses": 0,
    17: "favorite number"
}

> dict() = create or cast a dictionary

another_dictionary = dict(name = "Mojo", age = 6)

another_dictionary # {'name': 'Mojo', 'age': 6}

# accessing values in dictionaries

instructor = {
    "name": "Enzo",
    "owns_dog": False,
    "num_courses": 0,
    17: "favorite number"
}

> dictionary[key] = access individual key-values

instructor["name"] # "Enzo"

property = "owns_dog"
instructor[property] # False

instructor["random"] # KeyError because "random" is a non-existent key on instructor dictionary 

> for x in dictionary.items() = get a list of tuples of all of dictionary's key-values with a for loop

for item in instructor.items():
    print(item)

for key,value in instructor.items():
    print(f"{key} : {value}")

total_donations = 0

for k, v in donations.items():
    total_donations += v

> dictionary["key"] = value
>
> add a value to a pre-existing dictionary

instructor = {
    "name": "Enzo",
    "owns_dog": False,
    "num_courses": 0,
    17: "favorite number"
}

instructor["test"] = 100

> dictionary.keys(), dictionary.values() = gets keys & values respectively

for k in instructor.keys():
    print(k)

for value in instructor.values():
    print(value)

# dictionary key-value validation using in

instructor = {
    "name": "Enzo",
    "owns_dog": False,
    "num_courses": 0,
    17: "favorite number"
}

> "key" in dictionary

"name" in instructor # True
"test" in instructor # False

> "value" in dictionary.values()

0 in instructor.values() # True
"least favorite number" in instructor.values() # False

# dictionary methods

> dictionary.clear() = empties dictionary of all key-value pairs

person = dict(name="test", age=10)
person.clear() # {}

> dictionary.copy() = copies pre-existing dictionary of all key-value pairs

person = dict(name="test", age=10)
person_copy = person.copy() # {'name': 'test', 'age': 10}

person_copy is person # False because each dict is alloted to unique space in memory

person_copy == person # True because == tests for equality of values

> dictionary.fromkeys() = creates key-value pairs from comma seperated values

__used for setting default/initial state dictionaries__

{}.fromkeys(["email"], "unknown") # {'email': 'unknown'}
{}.fromkeys("a", [1,2,3]) # {'a': [1,2,3]}

new_user = {}.fromkeys(["name", "score", "email", "profile bio"], "unknown")

new_user # {'name': 'unknown', 'score': 'unknown', 'email': 'unknown', 'profile bio': 'unknown'}

__whatever the first argument passed will be iterated over as keys__

new_user.fromkeys('ab', 'unknown') # {'a': 'unknown', 'b': 'unknown'}

new_user.fromkeys(range(1,3), "wow") # {1: 'wow', 2: 'wow'}

> dictionary.get() = retrieves a key in an object and return None instead of a KeyError if the does not exist

__get() is more commonly used instead of in__

test_dict = dict(a=1, b=2, c=3)

test_dict.get("a") # 1

test_dict.get("no_key") # None

> dictionary.pop() = takes key argument and removes key-value pair from dictionary and also returns the value of removed key-value pair

instructor = {
    "name": "Enzo",
    "owns_dog": False,
    "num_courses": 0,
    17: "favorite number"
}

instructor.pop("owns_dog") # False

> dictionary.popitem() = removes random key-value pair from dictionary and also returns the value of removed key-value pair

instructor = {
    "name": "Enzo",
    "owns_dog": False,
    "num_courses": 0,
    17: "favorite number"
}

instructor.popitem() # (17, 'favorite number')

> dictionary.update() = updates key-value pair from dictionary with provided key-value pair

first = dict(a=1, b=2)
second = {}

__will add values if key is missing__

second.update(first) # {'a': 1, 'b':2}

__will also overide any value conflicts__

second["a": 0] # {'a': 0, 'b': 2}
second.update(first) # {'a': 1, 'b': 2}

__passing an empty dictionary does nothing__

second = dict(a=1, b=2)
second.update({}) # {'a': 1, 'b': 2}

# dictionary comprehension

> synatx explaination = key : value_logic for key, value in dictionary.items()
>
> {__:__for__in__}

__iterate over dictionary.keys() by default, but can use dictionary.items()__

numbers = dict(a=1, b=2)

sqr_nums = {key: value ** 2 for key, value in numbers.items()}

print(sqr_nums) # {'a':1, 'b':4}

> making a dictionary with dictionary comprehension

{num : num**2 for num in [1,2]} # {1:1, 2:4}

> using str with dictionary comprehension to create a dictionary

str1 = "abc"
str2 = "123"
combo = {str1[i]: str2[i] for i in range(0, len(str1))}

print(combo) # {'a': '1', 'b': '2', 'c': '3'}

> conditional logic with dictionary comprehension

num_list = [1,2,3,4]

{num : ("even" if num % 2 == 0 else "odd") for num in num_list}

{1: 'odd', 2: 'even', 3: 'odd', 4: 'even'}
