
import time

def timer(x):
    def f():
        y = time.time()
        x()
        z = time.time()
        print(z - y)
    return f


@timer
def hello():
    print("hello")

hello()

""" output is...
hello
0.0009634494781494141
"""