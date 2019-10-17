"""

aka Big-O notation

O(1) - constant
O(n) - linear
O(n^2) - quadratic
O(n^3) - cubic
O(n^*) - exponential
O(n log(n)) - n log n

Goal: Stay in the first 3 times (constant, linear, quadratic)


Linear:
    Number of items in the list, results in a linear number of executions

    for i in list:
        print(i)

N-square:
    for i in list:
            for j in list:

N-square:
    while True:
        for i in list:

"""
# EXAMPLES
"""
class UnorderedList:


    def add_item(self, new_item):
        1   temp = Node(new_item)
        1   temp.set_next(self.head)
        1   self.head = temp

    # this is O(1) - constant. Performs the same number of operations, no matter what args we pass.


    def length(self):
        1   count = 0
        1   current = self.head

        n   while current != None:
                count += 1 
                current = current.get_next()

        1 return count

    # this is O(n+3) - however, because n can theoretically climb to huge numbers, the 3 is insignificant
    # this boils down to O(n)


    def remove(self, item):
        1    current = self.head
        1    found = False
        1    previous = None

        n    while not found:
                if current.get_data() == item:
                1    found = True
                else:
                1    previous = current
                1    current = current.get_next()

            if previous == None:
            1    self.head = current.get_next()
            else:
            1    previous.set_next(current.get_next())

            return current

    # this is O(n)


def example():
    x = input("fjkds;jaf")

    if x > 10:
        for i in range(x):
            print(i)
    else:
        print(x)

    # The function has 1 of 2 outcomes:
        1) Input less than 10, only 1 execution                 O(1)  aka best case for performance
        2) Input greater than 10, high number of executions     O(n)  aka worst case for performance
    # Therefore, assume the worst
    # This is O(n)


def example():

    10  for x in range(10):
        35  for y in range(35):
            1   print(x + y)

    # This is O(1) - constant. Because we know exactly how many executions it will have.


def example():
    x = some list, don't know the specifics

    n   for i in x:
        n   for j in x:
            1   print("hi")

    # This is O(n^2) - quadratic. A nested iteration of unknown length. N-square.


"""