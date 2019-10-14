
def attempt_returning_multiple_vars(x, y):
    mult = x * y
    addition = x + y
    return mult, addition


ans_mult, ans_addiiton = attempt_returning_multiple_vars(5, 8)

print(ans_addiiton)
print(ans_mult)