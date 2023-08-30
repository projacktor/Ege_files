from fnmatch import fnmatch

# 1
for i in range(0, 10**9+1, 23):
    if fnmatch(str(i), '12345?7?8'):
        print(i, i // 23)

'''123450798 5367426
123451718 5367466
123453788 5367556
123454708 5367596
123456778 5367686
123459768 5367816'''


# 2
# def div(n):
#     dvs = set()
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             dvs.add(i)
#             dvs.add(n//i)
#     return sorted(dvs)
#
#
# cnt = 5
# for i in range(460_000_001, 460_000_000+1000):
#     d = [j for j in div(i)]
#     if len(d) >= 5:
#         print(i, d[-5])
#         cnt -= 1
#     if cnt == 0:
#         break

'''41818182
261959
5
271
57500001'''


# 3
# def div(n):
#     dvs = set()
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             dvs.add(i)
#             dvs.add(n//i)
#     return sorted(dvs)
#
#
# cnt = 5
# for i in range(11_000_001, 11_000_000+1001):
#     d = [j for j in div(i)]
#     if len(d) != 0:
#         m = d[-1] + d[-2]
#         if cnt == 0:
#             break
#         if 0 < m < 10_000:
#             print(i, m)
#             cnt -= 1

'''8672
8388
8532
7042
7364'''


# 4
# for i in range(0, 10**9, 2049):
#     if fnmatch(str(i), '32*21?4'):
#         print(i, i // 2049)

'''321992154 157146
324082134 158166
326172114 159186
329102184 160616'''

# 5
# def div(n):
#     dvs = set()
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             dvs.add(i)
#             dvs.add(n//i)
#     return sorted(dvs)
#
#
# cnt = 5
# for i in range(800_000, 0, -1):
#     d = [j for j in div(i)]
#     if len(d) != 0:
#         m = d[-1] - d[0]
#         if m % 23 == 0:
#             cnt -= 1
#             print(i , m)
#     if cnt == 0:
#         break

'''799995 266662
799990 399993
799987 16974
799944 399970
799907 27554'''


# 6
def div(n):
    dvs = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            dvs.add(i)
            dvs.add(n//i)
    return sorted(dvs)


cnt = 6
for i in range(650_001, 650_000+1000):
    d = [j for j in div(i)]
    if len(d) != 0 and len(div(d[-1])) != 0:
        print(i, d[-1])
        cnt -= 1
    if cnt == 0: break

'''650000 325000
650001 216667
650003 28261
650004 325002
650005 130001
650006 325003'''