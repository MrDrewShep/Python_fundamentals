
# this is O(n^2)

        
def insertion_sort(numbers):
    for i in range(1, len(numbers)):
        item_to_insert = numbers.pop(i)

        j = i - 1

        while j >= 0 and numbers[j] > item_to_insert:
            j -= 1

        numbers.insert((j + 1), item_to_insert)

mylist = [4, 6, 2, 12, 55, 6, 2, 483, 388, 1]

insertion_sort(mylist)
print(mylist)