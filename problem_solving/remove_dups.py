
# from ..data_structures.unordered_list import UnorderedList
# this relative import didn't work, so instead...

from unordered_list import UnorderedList

def remove_dups(linked_list):
    start = linked_list.head
    previous = None

    while start:
        my_next = start.get_next()
        previous = start

        while my_next:
            if start.get_data() == my_next.get_data():
                previous.set_next(my_next.get_next())
            previous = my_next
            my_next = my_next.get_next()

        start = start.get_next()

my_list = UnorderedList()
somestuff = [4, 2, 44, 23, 2, 3, 4, 9]

for i in somestuff:
    my_list.add_item(i)

print(my_list)
remove_dups(my_list)
print(my_list)