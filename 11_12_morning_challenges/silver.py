
from collections import OrderedDict
import itertools
import pprint

sen = "The quick brown fox jumped over the lazy dog."

odict = OrderedDict.fromkeys(sen)

x = ""
print(x.join(list(odict)))

# temp = odict.keys()

# print(temp)

# temp2 = itertools.chain.from_iterable(temp)

# pprint.pprint(temp2)

# # brute force below

new_sen = ""

for char in sen:
    new_sen += char if char == " " else char if char.lower() not in new_sen.lower() else ""

print(new_sen)

print("new solution below, inline comp")
print(char if char == " " else char if char.lower() not in new_sen.lower() else "" for char in sen)