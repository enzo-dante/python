# dictionaries = key-value pairs

> keys describe data, values represent the data
>
> keys are almost always strings or numbers, but values can be anything

instructors = {
    "name": "Enzo",
    "owns_dog": False,
    "num_courses": 0,
    17: "favorite number"
}

> dict() = create or cast a dictionary

another_dictionary = dict(name = "Mojo", age = 6)

another_dictionary # {'name': 'Mojo', 'age': 6}

# accessing values in dictionaries

instructors = {
    "name": "Enzo",
    "owns_dog": False,
    "num_courses": 0,
    17: "favorite number"
}

> dictionary[key] = access individual key-values

instructors["name"] # "Enzo"

instructors["random"] # KeyError because "random" is a non-existent key on instructors dictionary 

> for x in dictionary.items() = get a list of tuples of all of dictionary's key-values with a for loop

for item in instructors.items():
    print(item)

for key,value in instructors.items():
    print(f"{key} : {value}")

> dictionary.keys(), dictionary.values() = gets keys & values respectively

for k in instructors.keys():
    print(k)

for value in instructors.values():
    print(value)

# dictionary key-value validation using in

"instructors = {
    "name": "Enzo",
    "owns_dog": False,
    "num_courses": 0,
    17: "favorite number"
}

> "key" in dictionary

"name" in instructors # True
"test" in instructors # False

> "value" in dictionary.values()

0 in instructors.values() # True
"least favorite number" in instructors.values() # False

# dictionary methods

> dictionary.clear() = empties dictionary of all key-value pairs

person = dict(name="test", age=10)
person.clear() # {}

> dictionary.copy() = empties dictionary of all key-value pairs

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

> dictionary.get() = retrieves a key in an object and return None instead of a KeyError if the does not exist

__get() is more commonly used instead of in__

test_dict = dict(a=1, b=2, c=3)

test_dict.get("a") # 1

test_dict.get("no_key") # None