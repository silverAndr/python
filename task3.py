def my_func(arg1, arg2, arg3):
    my_list = [arg1, arg2, arg3]
    my_list.remove(min(my_list))
    return sum(my_list)

print(my_func(10, 2, 3))
