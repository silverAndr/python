def my_pow_2(x, y):
    r = x
    while y > 1:
        r = r * x
        y -= 1
    return r


print(my_pow_2(2, 8))
my_pow = lambda x, y: x**y
print(my_pow(2, 8))
