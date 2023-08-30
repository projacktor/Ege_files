# 1
# def div(n):
#     dvs = set()
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             dvs.add(i)
#             dvs.add(n // i)
#     return sorted(dvs)
#
#
# for i in range(174457, 174505+1):
#     d = [j for j in div(i)]
#     if len(d) == 2:
#         print(*d)
#         # res.append((i, d[0] * d[1]))

# 2
# def div(n):
#     dvs = set()
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             dvs.add(i)
#             dvs.add(n // i)
#     return sorted(dvs)
#
#
# for i in range(81_234, 134_689 + 1):
#     divd = [j for j in div(i)]
#     if len(divd) == 3:
#         print(*divd)

# 3
# def div(n):
#     dvs = set()
#     for i in range(1, int(n ** 0.5) + 1):
#         if n % i == 0:
#             dvs.add(i)
#             dvs.add(n // i)
#     return sorted(dvs)
#
#
# for i in range(15_40_26, 15_40_43+1):
#     dv = [j for j in div(i)]
#     if len(dv) == 4:
#         print(dv[2], dv[3])

# 4
# def div(n):
#     dvs = set()
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             dvs.add(i)
#             dvs.add(n // i)
#     return sorted(dvs)
#
#
# cnt = 0
# for i in range(150_000, 150_000+1000):
#     dv = [j for j in div(i)]
#     if sum(dv) % 13 == 10:
#         cnt += 1
#         print(i, sum(dv))
#     if cnt == 7:
#         break

# 5
# def div(n):
#     dvs = set()
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             dvs.add(i)
#             dvs.add(n // i)
#     return sorted(dvs)
#
#
# cnt = 0
# for i in range(250_200, 250_200 + 10000):
#     dv = [j for j in div(i)]
#     if dv != [] and (int(max(dv)) + int(min(dv))) % 123 == 17:
#         cnt += 1
#         print(i, dv[0] + dv[-1])
#     if cnt == 5:
#         break

# 6
# def div(n):
#     dvs = set()
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             dvs.add(i)
#             dvs.add(n // i)
#     return list(sorted(dvs))
#
#
# cnt = 0
# for i in range(550_000, 550_000 + 1001):
#     dv = div(i)
#     if dv != []:
#         f = sum(dv) // len(dv)
#         if f % 31 == 13:
#             cnt += 1
#             print(i, f)
#         if cnt == 5:
#             break

# 7
# def div(n):
#     dvs = set()
#     for _ in range(2, int(n ** 0.5) + 1):
#         if n % _ == 0:
#             dvs.add(_)
#             dvs.add(n // _)
#     return list(sorted(dvs))
#
#
# cnt = 0
# for i in range(400_000_000, 400_000_000 + 10000):
#     dv = div(i)
#     if len(dv) >= 5:
#         p = dv[0] * dv[1] * dv[2] * dv[3] * dv[4]
#         if p % 100 == 17 and p < i:
#             cnt += 1
#             print(p, dv[4])
#         if cnt == 5:
#             break

# 8
# def div(n):
#     dvs = set()
#     for i in range(1, int(n ** 0.5) + 1):
#         if n % i == 0:
#             dvs.add(i)
#             dvs.add(n // i)
#     return sorted(dvs)
#
#
# cnt = 0
# for i in range(190_201, 190_260 + 1):
#     dv = [j for j in div(i) if j % 2 == 0]
#     if len(dv) == 4:
#         print(dv[-1], dv[-2])

# 9
# def div(n):
#     dvs = set()
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             dvs.add(i)
#             dvs.add(n // i)
#     return sorted(dvs)


# for i in range(1_204_300, 1_204_380):
#     dv = [x for x in div(i) if x % 2 == 0]
#     if dv != []:
#         s = sum(dv)
#         if s % 10 == 0:
#             print(i, s)

# 10
# def div(n):
#     dvs = set()
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             dvs.add(i)
#             dvs.add(n // i)
#     return sorted(dvs)


# cnt = 0
# for i in range(500_000, 500_000 + 1001):
#     d = [j for j in div(i) if j % 10 == 8 and j != 8 and j != i]
#     if d != []:
#         cnt += 1
#         print(i, d[0])
#     if cnt == 5:
#         break

# 11
# def div(n):
#     dvs = set()
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             dvs.add(i)
#             dvs.add(n // i)
#     return sorted(dvs)
#
#
# cnt = 4
# for i in range(300_000, 300_000 + 1001):
#     dv = [j for j in div(i) if j % 3 == 0 and j != i]
#     if dv != []:
#         if len(dv) == 5:
#             cnt -= 1
#             print(i, dv[-1])
#         if cnt == 0:
#             break

# 12
# def div(n):
#     dvs = set()
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             dvs.add(i)
#             dvs.add(n // i)
#     return sorted(dvs)
#
#
# cnt = 5
# for i in range(550_000, 550_000 + 1001):
#     dv = [j for j in div(i) if j % 10 == 7]
#     if dv != []:
#         if len(dv) == 3:
#             cnt -= 1
#             print(i, dv[-1])
#         if cnt == 0:
#             break

# 13
# def div(n):
#     dvs = set()
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             dvs.add(i)
#             dvs.add(n // i)
#     return sorted(dvs)


# for i in range(6_080_068, 6_080_176+1):
#     dv = [j for j in div(i)]
#     # print(i, dv)
#     if len(dv) == 0:
#         print(i)

# 14
# def p(n):
#     return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))
# def div(n):
#     dvs = set()
#     for i in range(2, int(n*0.5) + 1):
#         if n % i == 0:
#             dvs.add(i)
#             dvs.add(n // i)
#     return sorted(dvs)
#
#
# for i in range(25_317, 51_237 + 1):
#     dv = [j for j in div(i) if len(div(j)) == 0]
#     if len(dv) == 6:
#         print(i, dv[-1])

# 15
# def div(n):
#     dvs = set()
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             dvs.add(i)
#             dvs.add(n // i)
#     return sorted(dvs)
#
#
# cnt = 7
# for i in range(500_000, 0, -1):
#     dv = [j for j in div(i) if len(div(j)) == 0]
#     if len(dv) != 0:
#         s = sum(dv)
#         if s % 10 == 0:
#             cnt -= 1
#             print(i, s)
#         if cnt == 0:
#             break

# 16
# def div(n):
#     dvs = set()
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             dvs.add(i)
#             dvs.add(n // i)
#     return sorted(dvs)
#
#
# for i in range(125_697, 125_721):
#     dv = [j for j in div(i) if len(div(j)) == 0]
#     if len(dv) == 2 and dv[0] * dv[1] == i:
#         print(dv[0], dv[1])

# 17
# def p(n):
#     return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))
#
#
# def div(n):
#     if p(int(n)) and n**4 in range(106_732_567, 152_673_836+1):
#         return True
#     else:
#         return False
#
#
# for i in range(int(106_732_567**0.25), int((152_673_836+1)**0.25)):
#     d = div(i)
#     if d:
#         print(i*i*i*i, i*i*i)

# 20
# def div(n):
#     dvs = set()
#     for i in range(1, int(n ** 0.5) + 1):
#         if n % i == 0:
#             dvs.add(i)
#             dvs.add(n // i)
#     return sorted(dvs)
#
#
# n = 2**4 * 3**4 * 5**4 * 7 * 11 * 13
# print(n)
# print(div(n))

# 19
# def div(n):
#     dvs = set()
#     cnt = 0
#     for i in range(1, int(n ** 0.5) + 1):
#         if cnt > 3:
#             break
#         if n % i == 0:
#             if i % 2 == 0:
#                 cnt += 1
#                 dvs.add(i)
#                 dvs.add(n // i)
#     return sorted(dvs)
#
#
# for i in range(113 * 10**6, 114 * 10**6 + 1):
#     d = div(i)
#     print(d)
