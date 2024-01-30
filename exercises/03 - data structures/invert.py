from random import random
import time

def invert(d):
    res = {}
    for k in d.keys():
        res[d[k]] = k
    return res

def print_time(f):
    def func(*args):
        start = time.time()
        result = f(args)
        end = time.time()
        print("Execution time:", round((end-start)*1000,6), "ms")
        
        return result
    return func

@print_time
def mocking(s):
    res = []
    for c in s:
        if random() < 0.5:
            res.append(c.lower())
        else:
            res.append(c.upper())
    return "".join(res)

s = "Hello World!"
print(mocking(s))
print("".join([c.lower() if random() < 0.5 else c.upper() for c in s]))
d = {"A":1, "B":2, "C":3}
print(d)
print(invert(d))