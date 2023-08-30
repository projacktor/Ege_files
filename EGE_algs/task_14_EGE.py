# 1
# s = 2 * 216**8 + 4 * 36**12 + 6**15 - 1296
#
#
# def ss(n):
#     st = ''
#     while n > 0:
#         st += str(n % 6)
#         n //= 6
#     return st[::-1]
#
#
# print(ss(s))
# print(ss(s).count('0'))

# 2
# s = 3 * 343**8 + 5 * 49**12 + 7**15 - 49
#
#
# def ss(n):
#     new = ''
#     while n > 0:
#         new += str(n % 7)
#         n //= 7
#     return new[::-1]
#
#
# n7 = ss(s)
# cnt = list(set(n7))
# print(cnt)
# # print(n7.count(cnt[0]), n7.count(cnt[1]), n7.count(cnt[2]))
# print(f"{n7.count(cnt[0])} - {cnt[0]} \n {n7.count(cnt[1])} - {cnt[1]} \n {n7.count(cnt[2])} - {cnt[2]}")

# 3
# for x in '012345678':
#     n = int('88' + x + '4' + x, 9) + int('7' + x + '344', 9)
#     if n % 67 == 0:
#         print(x)
#         print(n)
#         print(n // 67)

# 4
# for x in '0123456789ABCD':
#     m = int('8' + x + '12' + x, 14)
#     n = int('8' + x + '542', 14)
#     for a in range(1, 1000):
#         if (m + a) % n == 0:
#             print(a)
#             break

# 5
# for x in '0123456789':
#     n = int('3' + x + 'DA', 14) + int('5' + x + 'A6', 12)
#     if n % 81 == 0:
#         print(n // 81)

# 6
# for x in '0123456789A':
#     for y in '01234567':
#         try:
#             n = int(y + '04' + x + '5', 11) + int('253' + x + y, 8)
#             if n % 117 == 0:
#                 print(n // 117)
#         except ValueError:
#             ...


# hard 1

# def chet(n):
#     n8 = oct(n)[2:]
#     cnt = 0
#     for i in n8:
#         if int(i) % 2 == 0:
#             cnt += 1
#     if cnt <= 2:
#         return True
#     elif cnt > 2:
#         return False
#
#
# for x in '0123456789ABCDEF':
#     n = int('8569' + x, 16) + int('12' + x + '48', 16)
#     if chet(n):
#         print(x)
#         print(oct(n)[2:])

# answer = 2_275_735

# hard 2
# cnt = 0
# for x in range(0, 80):
#     n1 = 5 * x**4 + 5 * x**3 + 1 * x**2 + 1 * x**1 + 3 * x**0
#     n2 = 7 * 80**3 + x * 80**2 + x * 80**1 + 5 * 80**0
#     razn = max(n1, n2) - min(n1, n2)
#     if razn <= 1_000_000:
#         cnt += 1
# print(cnt)

# answer = 4
