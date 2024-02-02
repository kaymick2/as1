from functools import lru_cache
import time
import matplotlib
import matplotlib.pyplot as plt 
import numpy
global timelis
global seekorder
timelist=[]
seekorder=[]

def timer(func):
    def wrapper(*args, **kwargs):
        start=time.perf_counter()
        result=func(*args, **kwargs)
        end=time.perf_counter()
        timelist.append(end-start)
        seekorder.append(args[0])
        print (f"Finished in {end - start:.8f}  seconds: f({args[0]}) -> {result}")
        return result
    return wrapper
    
@lru_cache
@timer
def fib(n:int)->int:
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)

        
if __name__=="__main__":
    fib(100)

plt.plot(seekorder, timelist) 
plt.show() 