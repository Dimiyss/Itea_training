date_1 = (1, 5, 2000)
date_2 = (5, 3, 2010)

data = (8, 10, 2005)

def check_include(data_1: tuple, data_2: tuple, data: tuple) -> bool:
    for val in range(len(data), -1, -1):
        if data[val] < data_1[val] or data[val] > data_2[val]:
            return False
