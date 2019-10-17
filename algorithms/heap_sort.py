
# This is O(n log(n))

def heapify(numbers, heap_size, root_index):
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    if left_child < heap_size and numbers[left_child] > numbers[largest]:
        largest = left_child

    if right_child < heap_size and numbers[right_child] > numbers[largest]:
        largest = right_child

    if largest != root_index:
        numbers[root_index], numbers[largest] = numbers[largest], numbers[root_index]
        heapify(numbers, heap_size, largest)


def heap_sort(numbers):
    n = len(numbers)

    for i in range(n, -1, -1):
        heapify(numbers, n, i)

    for i in range(n - 1, 0 , -1):
        numbers[i], numbers[0] = numbers[0], numbers[i]
        heapify(numbers, i, 0)

