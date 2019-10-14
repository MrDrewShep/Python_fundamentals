x = 'Drew'                  # String uses ' or "

age = 25                    # Integer
bowling_average = 225.8     # Float, anything with an average
miscvar = 1 + 2j            # Complex number, don't worry you won't likely use this

is_adult = True             # Boolean ( True or False ), capitalization matters

answer = 23 + 23            # Addition operator
answer = 23 - 23            # Subtraction
answer = 23 * 23            # Multiplication
answer = 23 / 23            # Division
                            # Python, where applicable, will change integers into floats coming out of an arithmatic operator ( type conversion )
answer = 12 % 5             # Modulus, returns the remainder of a division ( answer here is 2 )
answer = 2 ** 3             # Exponent, two to the power of three, 2 x 2 x 2
answer = 34 // 4            # Floor divison, throws away the remainder/decimal (answer here is 8 )

score = 0

score += 1                  # Plus equals, score = score + 1
score -= 1
score *= 2
score /= 5
score %= 3
score **= 2
score //= 2

first_name = 'Drew'
last_name = 'Shepherd'
full_name = first_name + ' ' + last_name        # Concatenation, + is the only arithmatic operator allowed
print(full_name)

greeting = f'Hello, my name is {first_name}.'  # F-string, allows you to inject variables into a string, f-string provides best performance
                                               # Saves us from having to do multiple concatenations
print(greeting)
                                               # You can also inject any valid Python code
greeting = f'Hello, my name is {12 + 12}.'
print(greeting)
greeting = 'Hello, my name is {}.'.format(first_name)   # Older way of typing this
print(greeting)

name = input('What\'s your name, brah? ')      # Don't forget space, alligator, space
age = int(input('You got an age? '))           # All inputs are interpreted as a STRING, unless cast otherwise

print('Hello', name)                            # Print statement, when vars are separated by a comma, will all be printed with a                                                   space in between
response = f'Hello, {name}! Sup?!'
print(response)
print('Hello' + ' ' + name)
print('You are', age)
age += 1
print('You are now', age)

my_string = "-23.25"
my_float = float(my_string)     # Converts to a float   int()  float()  str()
my_string2 = str(my_string)     # Converts to a string
my_int = int(my_float)         # This will chop the remainder
print(my_int)

# PUZZLE

total = 0

total += 1
# total = 1
# expression = (what is returned by the code) = (null)

total // 3
# total = 1
# expression = 0

total += (2 // 3) + 3
# total = 4
# expression = (null)

total + total
# total = 4
# expression = 8
