# 1
# def f(x, a):
#     return (x & 105 == 0) <= ((x & 58 != 0) <= (x & a != 0))
#
# for a in range(1, 10**4):
#     if all(f(x, a) for x in range(10**4)):
#         print(a)
#         break
# #answer 18


# 2
# def f(a, x):
#     return (x & 51 == 0) or ((x & 41 == 0) <= (x & a  == 0))
#
# for a in range(10**4):
#     if all(f(a, x) for x in range(10**4)):
#         print(a)
#         break
# answer 0


# 6
# def f(a, x):
#     return (a % 40 == 0) and ((780 % x == 0) <= ((a % x != 0) <= (180 % x != 0)))
#
# for a in range(1, 10**4):
#     if all(f(a, x) for x in range(1, 10**4)):
#         print(a)
#         break
# answer 120


# 7
# def f(a, x):
#     return ((x % 2 == 0) <= (x % 3 != 0)) or (x + a >= 100)
#
# for a in range(1, 10**4):
#     if all(f(a, x) for x in range(1, 10**4)):
#         print(a)
#         break
# answer 94



# 9
# def f(a, x, y):
#     return ((x + y <= 22) or (y <= x - 6) or (y >= a))
#
# for a in range(10**3):
#     if all(f(a, x, y) for x in range(10**3) for y in range(10**3)):
#         print(a)
# #answer 9


# 3
# def f(x, P, Q, a):
#     return (x in P) <= (not((x in P) == (x in Q)) or ((x in Q)) <= (x in a))
#
# P = list(range(69, 92))
# Q = list(range(77, 115))
# a = []
# for x in range(10**4):
#     if ((x in P) <= (not((x in P) == (x in Q)) or ((x in Q)) <= (x in a))) is False:
#         a.append(x)
# print(*a)
#answer 14
#


# 4
# P = list(range(24, 50))
# Q = list(range(30, 54))
# a = list(range(0, 100))
# for x in range(0, 100):
#     if ((x in a) <= (x in P) or (x in Q)) is False:
#         a.remove(x)
# print(*a)
#answer 29


# 5
# def f(x, y, a):
#     return (2 * x + y != 70) or (x < y) or (a < x)
# #
# # for a in range(100, -1, -1):
# #     if all(f(x, y, a) for x in range(100) for y in range(100)):
# #         print(a)
# #         break
# # #answer 23
#
# for a in range(10**3):
#     Flag = True
#     for x in range(10**3):
#         for y in range(10**3):
#             if not f(x, y, a):
#                 Flag = False
#                 break
#         if not Flag:
#             break
#     if Flag:
#         print(a)
# # right


#8
# p = list(range(44, 50))
# q = list(range(28, 54))
# a = list(range(0, 100))
# for x in range(0, 100):
#     if (((x in a) <= (x in p)) or (x in q)) is False:
#         a.remove(x)
# print(*a)
# # answer 25 (53 - 28)


# 10
# def pre(n, m):
#     return n % m == 0
#
# b = list(range(20, 81))
# a = list()
# for x in range(1, 100):
#     if ((x in b) <= (pre(x, 17) <= (x in a))) is False:
#         a.append(x)
# print(a)
# answer 34


# 11
# def f(a, x):
#     return (x & 85 == 0) <= ((x & 54 != 0) <= (x & a != 0))
#
# for a in range(10**3):
#     if all(f(a, x) for x in range(10**3)):
#         print(a)
#         break
# answer 34


# 12
# def f(a, x):
#     return (x & 49 == 0) <= ((x & 28!= 0) <= (x  & a != 0))
#
# for a in range(10**3):
#     if all(f(a, x) for x in range(10**3)):
#         print(a)
#         break
# answer 12


# 13
# p = list(range(69, 92))
# q = list(range(77, 115))
# a = []
#
# for x in range(200):
#     if ( (x in q) <= (((x in p) == (x in q)) or ((x not in p) <= (x in a))) ) is False:
#         a.append(x)
# print(*a)
# Answer 23


#14
# p = list(range(19, 85))
# q = list(range(4, 52))
# a = []
# for x in range(10**3):
#     if ((x in p) <= ((x not in q) <= ((x not in p) or (x in a)))) is False:
#         a.append(x)
# print(*a)
# answer 33


# 15
# def f(a, x, y):
#     return (3 * x + 7 * y < a) or ( x >= y) or (y > 6)
#
# for a in range(10**3):
#     if all(f(a, x, y) for x in range(10**3) for y in range(10**3)):
#         print(a)
#         break
# answer 58


# 16
# def f(a, x):
#     return ((x % 3 == 0) <= (x % 5 != 0)) or (x + a >= 90)
#
# for a in range(1, 10**4):
#     if all(f(a, x) for x in range(1, 10**4)):
#         print(a)
#         break
#  answer 75


# 17
# def f(a, x):
#     return (120 % a == 0) and ((x % 36 == 0) <= ((x % a != 0) <= (x % 45 != 0)))
#
# for a in range(1, 10**4):
#     if all(f(a, x) for x in range(1, 10**4)):
#         print(a)
# answer 60