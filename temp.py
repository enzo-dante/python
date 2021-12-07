import pdb

first = "first"
second = "second"

'''
common pdb commands:
    l (list)
    n (next line is most common command since it allows for stepping through)
    p (print)
    c (continue - finishes debugging)

'''

pdb.set_trace()

'''
can explore already defined values while in pdb viewer

first = 'first'

third = NameError: name 'third' has not been defined


'''

result = first + second

third = "third"
result += third
print(result)
