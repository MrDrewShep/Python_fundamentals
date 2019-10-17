
my_items = [1, 2, 3, 6, 89]

def recursive_sum(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        return numbers[0] + recursive_sum(numbers[1:])

print(recursive_sum(my_items))
print(sum(my_items))


# Fibonacci rules
# Starts with 0, 1
# Subsequent numbers are the sum of the previous two

def fib(numbers, current=1, previous=0, count=0):
    if count < numbers:
        return fib(numbers, current+previous, current, count + 1)
    else:
        return current


print(fib(5))

# Place a penny on a square of a chess board
# On each square, place an amount double to the amount on the previous square
# Total the amount on the board



def chess(square, money=0.01):
    if square == 0:
        return 0.0
    else:
        return money + chess(square - 1, money * 2)

print(chess(64))