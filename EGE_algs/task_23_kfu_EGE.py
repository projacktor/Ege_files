from functools import lru_cache
from sys import setrecursionlimit


setrecursionlimit(10**6)

# def calc(crr, end):
#     if crr < end: return 0
#     if crr == end: return 1
#     if crr > end: return calc(crr - 2, end) + calc(crr // 2, end)
#
#
# # print(calc(28, 10))
# # print(calc(10, 1))
# print(calc(28, 10) * calc(10, 1))
# # answer 36
#
#
# def calc(crr, end):
#     if crr < end: return 0
#     if crr == end: return 1
#     if crr > end: return calc(crr - 1, end) + calc(crr // 2, end)
#
#
# print(calc(30, 12) * calc(12, 1))
# # answer 376
#
# @lru_cache(None)
# def calc(crr, end):
#     if crr > end:
#         return 0
#     if crr == end:
#         return 1
#     if crr < end:
#         return calc(crr + 1, end) + calc(crr + 2, end) + calc(crr * 3, end)
#     ...
#
#
# print(calc(1, 10) * calc(10, 15))
# # answer 672
#
# def calc(crr, end):
#     if crr > end or crr == 12: return 0
#     if crr == end: return 1
#     if crr < end: return calc(crr + 1, end) + calc(crr + 2, end) + calc(crr * 3, end)
#
#
# print(calc(2, 9) * calc(9, 19))
# # answer 650
#
# def calc(crr, end):
#     if crr > end or crr == 30: return 0
#     if crr == end: return 1
#     if crr < end:
#         return calc(crr + 1, end) + calc(crr * 2, end) + calc(crr * 3, end)
#
#
# print(calc(2, 13) * calc(13, 39))
# # answer 75
#
# def calc(crr, end, flag):
#     if crr > end: return 0
#     if crr == end: return 1
#     if crr < end and not(flag):
#         return calc(crr + 1, end, False) + calc(crr + 2, end, False) + calc(crr * 2, end, True)
#     if crr < end and flag:
#         return calc(crr + 1, end, False) + calc(crr + 2, end, False)
#
#
# print(calc(1, 9, False))
# answer 77

# @lru_cache(None)
# def calc(crr, end, step):
#     if crr > end or step == 30: return 0
#     if crr == end and step != 30: return 1
#     if crr < end: return calc(crr + 1, end, step + 1) + calc(crr * 2, end, step) + calc(crr * 3, end, step)
#
#
# print(calc(1, 9217, 0))
# answer 71345242 wrong


# def calc(crr, end, flag):
#     if crr > end: return 0
#     if crr == end: return 1
#     if crr < end and flag:
#         return calc(crr + 1, end, False) + calc(crr * 2, end, True)
#     if crr < end and not(flag):
#         return calc(crr + 1, end, True) + calc(crr * 2, end, False)
#
#
# print(calc(1, 14, True))
# answer 26 wrong

# @lru_cache(None)
# def calc(crr, end):
#     if crr < end: return 0
#     if crr == end: return 1
#     if crr > end: return calc(crr - 3, end) + calc(crr // 7, end)
#
#
# print(calc(50, 1))
# answer 6