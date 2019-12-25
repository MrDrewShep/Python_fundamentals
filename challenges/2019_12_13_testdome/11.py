try:
    myvar = open("fjkds;f;la", "r")
    print('made it this far')
except FileNotFoundError as e:
    print('houston we have a problem', e.strerror)
    print(myvar, type(myvar))
finally:
    print('never seen a finally statement before')