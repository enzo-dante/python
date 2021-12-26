# iterators & iterables

> an object which can be iterated upon & returns data one element at a time when next() is called upon in the background
def my_for_loop(iterable):
    iterator = iter(iterable)

    while True:
       try:
> an object which will return an iterator when iter() is called in the background
            thing = next(iterator)
> an iterator will stop when it raises a stopIteration error
        except StopIteration:
            break
        else:
            func(thing) # print

my_for_loop("lol" my print)

# custom iterators

__the class below overrides dunder methods__

class Counter:

    def __init__(self, low, high):
        self.current= low,
        self.high = high

    def __iter__(self):
        return iter("test")

    def __next__(self):
        if self.current < self.high:
            num = self.current
            self.current += 1
            return num

        raise StopIteration

> the for loop will call iter(Counter(0,10)) and __iter__ will call itself

for n in Counter(0,10):
    print(n)

# generators from generator functions

> all generators are iterators that create a generator quickly and the generator iterable yields the value, to iterate over it you would need next()
>
> not all iterators are generators though

def count_up_to(max):
    count = 1

__functions use RETURN, generator functions use YIELD__

    while count <= max
        yield count # for generators, calling yield stops the execution and won't resume until next() is called
        count +=

__functions return once, generator functions can yield multiple values__

count = count_up_to(5)
print(next(count)) # 1

for n in count:
    print(n) # 0,1,2,3,4

# infinite generators

> since lists take a lot of memory as they grow, if you only need one item from that list, use a generator

def current_beat():

    # 4-count in music
    nums = (1,2,3,4)
    index = 0

    # infinite generator
    while True:

        # reset
        if i >= len(nums): i = 0
        yield nums[i]
        i += 1

count = current_beat()

__calling next() on count will continue forever in example, but only dealing with 1 number at a time__

next(count)

# generator expressions

> create generators from generator expressions with simpler syntax that use ()

__defined generator__

def nums():
    for num in range(1,10):
        yield num

g = nums()

__generator expression__

g2 = (num for num in range(1,10)) # g2 = generator object

__generator expression with sum()__

total = sum(num for num in range(1,10)) # total = generator object
