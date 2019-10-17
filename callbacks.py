
def im_gonna_be_a_callback(x):
    print(x)

def i_take_callbacks(cb):
    cb("Hello world")

i_take_callbacks(im_gonna_be_a_callback)
