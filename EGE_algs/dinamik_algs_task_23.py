from sys import setrecursionlimit
from functools import lru_cache

# setrecursionlimit(10**6)


# @lru_cache(None)
# def calc(crr, end):
#     if crr > end:
#         return 0
#     if crr == end:
#         return 1
#     if crr < end:
#         return calc(crr + 1, end) + calc(crr * 2, end) + calc(crr * crr, end)


# print(calc(5, 154))


# dp = [0 for _ in range(1000)]
# dp[5] = 1
# for i in range(5, 154):
#     if i + 1 <= 154:
#         dp[i+1] += dp[i]
#
#     if i * 2 <= 154:
#         dp[i*2] += dp[i]
#
#     if i*i <= 154:
#         dp[i*i] += dp[i]

# print(dp[154])