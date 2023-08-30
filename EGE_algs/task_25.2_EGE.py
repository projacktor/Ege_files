# kompege
# 1
'''способ 1. Медленный fnmatch'''
# from fnmatch import *
# for x in range(0, 10**9, 17):
#     if fnmatch(str(x), '12345?6?8'):
#         print(x, x // 17)

'''способ 2. Цилклический перебор'''
# for i in '0123456789':
#     for j in '0123456789':
#         n = int(f"12345{i}6{j}8")
#         if n % 17 == 0:
#             print(n, n // 17)

from fnmatch import fnmatch
# 2
# for n in range(0, 10 ** 8, 141):
#     if fnmatch(str(n), '1234*7'):
#         print(n, n // 141)

# 3
# for n in range(0, 10**9, 169):
#     if fnmatch(str(n), '123*567?'):
#         print(n, n // 169)
''' рассматриваем 3 случая для "123*567?". На месте * либо пустота либо произвольное кол-во цифр
на месте ? одна произвольная цифра. => тк в цисле известны 6 цифр + 1 фиксированный знак вопроса
и тк ограничение в 10**9 элементов
у нас может быть 7, 8, 9 элементов в числе
 (9 - 7 = максимум сколько можно поставить вместо *, то есть, либо 0 элем, либо 1, либо 2)'''
# for i in '0123456789':
#     n = int(f"123567{i}")
#     if n % 169 == 0:
#         print(n, n // 169)
# for i in '0123456789':
#     for j in '0123456789':
#         n = int(f"123{i}567{j}")
#         if n % 169 == 0:
#             print(n, n // 169)
# for i in '0123456789':
#     for j in '0123456789':
#         for y in '0123456789':
#             n = int(f"123{i}{j}567{y}")
#             if n % 169 == 0:
#                 print(n, n // 169)

# 4
# for i in '0123456789':
#     n = int(f"12{i}45")
#     if n % 51 == 0:
#         print(n, n // 51)
# for i in '0123456789':
#     for j in '0123456789':
#         n=int(f"12{i}{j}45")
#         if n % 51 == 0:
#             print(n, n // 51)
# for i in '0123456789':
#     n = int(f"1245{i}")
#     if n % 51 == 0:
#         print(n, n // 51)
# for i in '0123456789':
#     for j in '0123456789':
#         n = int(f"1245{i}{j}")
#         if n % 51 == 0:
#             print(n, n // 51)
# for i in '0123456789':
#     for j in '0123456789':
#         n = int(f"12{i}45{j}")
#         if n % 51 == 0:
#             print(n, n // 51)
# n = int(f"1245")
# if n % 51 == 0:
#     print(n, n // 51)

# 5
# for i in range(0, 10**10, 2023):
#     if fnmatch(str(i), '1?2139*4'):
#         print(i, i // 2023)

# 6
# def div(n):
#     dvs = set()
#     for i in range(1, int(n ** 0.5) + 1):
#         if n % i == 0:
#             dvs.add(i)
#             dvs.add(n // i)
#     return sorted(dvs)
#
#
# # cnt = 7
# for i in range(65000, 65000 + 1000000):
#     if fnmatch(str(i), '6*97*5?'):
#         d = [j for j in div(i) if j % 2 == 0]
#         if len(d) >= 4:
#             # cnt -= 1
#             print(i, sum(d))
#         # if cnt == 0:
#         #     break

# 7
# def div(n):
#     dvs = set()
#     for i in range(1, int(n**0.5)+1):
#         if n % i == 0:
#             dvs.add(i)
#             dvs.add(n//i)
#     return sorted(dvs)
#
# from fnmatch import fnmatch
# qnt = []
# for i in range(10**7):
#     if fnmatch(str(i), '9?*55*7'):
#         # print(i)
#         qnt.append(i)
# qnt[:] = qnt[::-1]
# qnt[:] = qnt[:5][::-1]
# # print()
# for i in qnt:
#     print(i, sum(div(i))%21)

# 8
# from fnmatch import fnmatch
#
#
# def div(n):
#     dvs = set()
#     for i in range(1, int(n**0.5) + 1):
#         if n % i == 0:
#             dvs.add(i)
#             dvs.add(n//i)
#     return sorted(dvs)
#
#
# cnt = 0
# for i in range(10**7):
#     if fnmatch(str(i), '?6*6*?6') and i % 8 == 0 and i % 7 == 0 and i % 6 == 0:
#         cnt += 1
#         print(i, sum(div(i)))
#     if cnt == 7:
#         break

# 9
# from fnmatch import fnmatch
#
#
# def div(n):
#     dvs = set()
#     for i in range(1, int(n**0.5) + 1):
#         if n % i == 0:
#             dvs.add(i)
#             dvs.add(n//i)
#     return sorted(dvs)
#
#
# for i in range(217, 10**7, 217):
#     if fnmatch(str(i), '14?4*'):
#         d = [i for i in div(i) if i % 2 != 0]
#         print(i, sum(d))

