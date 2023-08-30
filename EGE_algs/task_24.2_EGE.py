# 12
# s = open("Task files/24.txt").readline().strip()
# # print(s)
# cnt = 1
# last = 0
# for i in range(len(s) - 1):
#     if int(s[i]) < int(s[i + 1]):
#         cnt += 1
#     else:
#         last = max(cnt, last)
#         cnt = 1
# print(last)

# 13
# s = open("Task files/24.txt").readline().strip()
# c = m = s[0]
# for i in range(1, len(s)):
#     if s[i] < s[i-1]:
#         c += s[i]
#         m = max(c, m, key=len)
#     else:
#         c = s[i]
# print(m)
# for i in m:
#     print(ord(i))

# 14 DD-подстрока ВАЖНО
# s = open("Task files/24.txt").readline()
# mn = 10**6
# while 'D' in s:
#     s = s.replace('D', ' ')
# s = s.split()
# # s = s[1:-1]
# for i in s:
#     if i != '':
#         mn = min(len(i) + 2, mn)
# print(mn)

# 15
# s = open("Task files/24.txt").readline().strip()
# mn = 10**6
# cnt = 0
# a = []
# for i in range(len(s)):
#     if s[i] == 'D':
#         cnt += 1
#     elif s[i] != 'D' and cnt != 0:
#         a.append(cnt)
#         cnt = 0
# mn = 10**6
# for i in a:
#     if i != 0:
#         mn = min(i, mn)
# print(mn)
# print(min(a))

# 16
# s = open("Task files/24.txt").readline()
# m = 0
# s = s.split('A')
# for i in range(len(s)-1):
#     st = s[i] + 'A' + s[i+1]
#     m = max(len(st), m)
# print(m)

# 17
# s = open("Task files/24.txt").readline()
# s = s.split('D')
# m = 0
# for i in range(len(s) - 2):
#     st = s[i] + 'D' + s[i + 1] + 'D' + s[i + 2]
#     m = max(len(st), m)
# print(m)

# 18
# s = open("Task files/24.txt").readline()
# while 'KOT' in s:
#     s = s.replace('KOT', '#')
# # print(s)
# cnt = 0
# m = 0
# for i in range(len(s)):
#     if s[i] == '#':
#         cnt += 1
#     else:
#         m = max(m, cnt)
#         cnt = 0
# print(m)

# print('W X Y Z | f')
# for w in 0,1:
#     for x in 0, 1:
#         for y in 0, 1:
#             for z in 0, 1:
#                 f = (((z <= y) and ((not x) <= w)) <= ((z == w) or (y and (not x))))
#                 if w == 0:
#                     continue
#                 if not f:
#                     print(w, x, y, z, "|", int(f))

# 5
# for n in range(1, 1000):
#     r = bin(n)[2:]
#     if n % 2 == 0:
#         r += '10'
#     else:
#         r = '1' + r + '01'
#     r = int(r, 2)
#     if r > 516:
#         break
#         print(n)
# 8
# from itertools import permutations
# cnt = 0
# for i in permutations('СПОРТЛОТО'):
#     s = ''.join(i)
#     if 'ОО' in s:
#         cnt += 1
#         # print(s, len(s))
# print(cnt)
# 12
# def redactor(s):
#     while '111' in s or '333' in s:
#         if '111' in s:
#             s = s.replace('111', '3', 1)
#         else:
#             s = s.replace('333', '1', 1)
#     return int(s)
# mn = 10**6
# cnt = 0
# for i in range(100, 500):
#     s = i * '3'
#     st = redactor(s)
#     if st < mn:
#         mn = st
#         cnt = i
#     if mn == 1:
#         print(i)
#         break
# print(mn, i)
# 14
# for x in '0123456789abcdefg':
#     a = int('66' + '4' + '63', 17) - int('5' + "4" + '810', 17)
#     if a % 11 == 0:
#         print(a / 11)
# 15
# def f(a, x):
#     return (((x % 175 == 0) <= (x % 25 != 0)) or ((2 * x + a) >= 1780))
#
#
# c = 0
# for a in range(1, 10**4):
#     if all(f(a, x) for x in range(1, 10**4)):
#         print(a)
#         c = a
#         break
# print(all(f(c, x) for x in range(1, 10**4)))
# 16
# from functools import lru_cache
# @lru_cache(None)
# def f(n):
#     if n < 2:
#         return n
#     if n >= 2 and n % 2 == 0:
#         return f(n / 2) + 1
#     if n >= 2 and n % 2 != 0:
#         return f(3*n + 1) + 1
#
#
# cnt = 0
# for i in range(1, 100001):
#     if f(i) == 16:
#         cnt += 1
# print(cnt)
# 17
# s = list(map(int, open("Task files/17-332.txt")))
# seven = []
# ans = []
# for i in s:
#     if i % 17 == 0:
#         seven.append(i)
# savg = sum(seven)/len(seven)
#
#
# def digit_sum(n):
#     return sum(map(int, str(n)))
#
#
# for i in range(len(s) - 3):
#     if digit_sum(s[i]) == digit_sum(s[i+2]) and s[i+1] < savg:
#         ans.append(digit_sum(s[i+1]))
# print(len(ans))
# d = {f"{digit} counted": s.count(digit) for digit in sorted(set(s))}
# mx = 0
# smx = ''
# # print(d)
# for k, v in d.items():
#     if v > mx:
#         mx = v
#         smx = k
# 18
# print(smx, mx)
