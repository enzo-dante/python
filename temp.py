'''
list_manipulation([1,2,3], "remove", "end") # 3
list_manipulation([1,2,3], "remove", "beginning") #  1
list_manipulation([1,2,3], "add", "beginning", 20) #  [20,1,2,3]
list_manipulation([1,2,3], "add", "end", 30) #  [1,2,3,30]
'''

add = "add"
remove = "remove"
end = "end"
beginning = "beginning"

def list_manipulation(the_list, command, location, value=0):
    if command == remove and location == end:
        return the_list.pop()
    elif command == remove and location == beginning:
        return the_list.pop(0)
    elif command == add and location == beginning:
        # must make copy of the list before adding to it, it will return None if you try to add to argument
        new_list = [value]
        new_list.extend(the_list)
        return new_list
    elif command == add and location == end:
        # must make copy of the list before adding to it, it will return None if you try to add to argument
        list_copy = the_list
        list_copy.append(value)
        return list_copy

print(list_manipulation([1,2,3], "add", "end", 30))
