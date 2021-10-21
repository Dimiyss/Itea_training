# import requests
# from time import time_ns
#
#
# def benchmark(func):
#     def worker():
#         start = time_ns()
#         res = func()
#         print(f'time elapsed = {time_ns() - start} ns.')
#         return res
#     return worker
#
# # @benchmark
# def fetch_webpage():
#     return requests.get('https://google.com').headers
#
# fetch_webpage = benchmark(fetch_webpage)
#
# print(fetch_webpage())
# # ..
# print(fetch_webpage())
# # ..
# print(fetch_webpage())
