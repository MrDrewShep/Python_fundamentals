
# this is O()
# This could/should be refactored, rather than pass args through to track where we are in total, +/- currentl location in the lines the call recursion, to sum total where we are

def binary_search(numbers, item, first=0, last=None):
    if not last:
        last = len(numbers) - 1

    if item == numbers[first]:
        return 0
    elif item == numbers[last]:
        return last
    
    midpoint = (first + last) // 2

    if item == numbers[midpoint]:
        return midpoint
    elif item > numbers[midpoint]:
        return binary_search(numbers, item, midpoint + 1)
    elif item < numbers[midpoint]:
        return binary_search(numbers, item, first + 1, midpoint - 1)


my_list = [5, 7, 2, 12, 66, 543, 2, 4, 8, 75, 35, 3, 43, 23, 42]
my_list = sorted(my_list)
print(my_list)

print(binary_search(my_list, 543))