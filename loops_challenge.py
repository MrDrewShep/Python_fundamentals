puzzle = open("frequencies.txt", "r").read().split("\n")    # This import created a giant list of strings
numbers = [ int(i) for i in puzzle ]

numbers = [ int(i) for i in open("frequencies.txt", "r").read().split("\n") ]  # Condensed version

# List comprehension (behind the scenes is a for loop). A cheeky one line of code that turns something into a list. See below:
# numbers = []
# for i in puzzle:
#     numbers.append(int(i))

# PUZZLE
# 1a, change the first two lines into a single line of code
# 1b, What is the final frequency?
# 1b, (i) for loop (ii) while loop (iii) python built in

frequency = 0
for freq in numbers:
    frequency += freq
print(frequency)

frequency = 0
x = 0
while x < len(numbers):
    frequency += numbers[x]
    x += 1
print(frequency)

print(sum(numbers))

total_change = 0
for freq in numbers:
    total_change += abs(freq)
print(total_change)