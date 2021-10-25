# global_var = 10
#
# print(global_var)
#
# def test_func():
#     global global_var
#     print(global_var)
#
#     global_var += 1
#     print(global_var)
#
# test_func()




# def func_1():
#
#     local_test_var = 5
#
#     def helper():
#         nonlocal local_test_var
#
#         print(local_test_var)
#         local_test_var += 1
#         print(local_test_var)
#
#     helper()
#
# func_1()


def counter():
    i = 0
    def incrementer():
        nonlocal i
        i += 1
        return i
    return incrementer

c = counter()

print(c())
print(c())
print(c())


# if __name__ == '__main__':



