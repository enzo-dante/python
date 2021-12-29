
from functools import wraps
from time import time
def speed_test(fn):
    
    @wraps(fn) # wraps preserve "fn" metadata
    def wrapper(*args, **kwargs):
        start_time = time()
        result = fn(*args, **kwargs)
        end_time = time()
        print(f"Time Elapsed: {end_time - start_time}")
        return result
        
    return wrapper

@speed_test
def sum_nums_generator():
    return sum(x for x in range(1000000))

@speed_test
def sum_nums_list():
    return sum([x for x in range(1000000)])

print(sum_nums_generator())
print(sum_nums_list())