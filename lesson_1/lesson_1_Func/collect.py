# from copy import copy, deepcopy
#
# l1 = [1, 2, 3, [1, 2, 3]]
# l2 = deepcopy(l1)
#
# l1[3].append(4)
#
# print(l1)
# print(l2)

# l1 = [1, 2, 3, [1, 2, 3]]
# l2 = l1[:]
#
# print(l1)
# print(l2)
#
# l1[3].append(4)
#
# print(l1)
# print(l2)



#################################
# a = [1, 2, 3, 4, 5]
# b = (1, 2, 3, 4, 5)
#
# print(a.__sizeof__())
# print(b.__sizeof__())
# ###################################

# a = [1, 1, 2, 3 ,5, 4, 5 ,6 ,4 ,1 ,2 ,3 ,5 ,4]
# print(list(set(a)))

# ##########################

# l = []
#
# for i in range(10):
#     if i % 2:
#         l.append(i)
#
# print(l)
#
# l2 = [i for i in range(10) if i % 2]
# print(l2)

# d1 = {k: str(k) for k in range(10)}
# print(d1)
# print(d1[2])

d = dict.fromkeys(['a', 'b'])
print(d)

d = dict.fromkeys(['a', 'b'], 100)
print(d)


i = 0
i = i + 1
i += 1