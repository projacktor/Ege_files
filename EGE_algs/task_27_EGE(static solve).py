# 4
# with open("../Task files/27th files/27B_2721.txt") as file:
#     k5 = 0
#     k0 = 0
#     k2 = 0
#     k1 = 0
#     n = int(file.readline())
#     div5 = []
#     for _ in range(n):
#         num = int(file.readline())
#         if num % 5 == 0:
#             div5.append(num)
#         elif num % 2 == 0:
#             k2 += 1
#         elif num % 2 != 0:
#             k1 += 1
#
#     for i in div5:
#         if i % 10 == 5:
#             k5 += 1
#         elif i % 10 == 0:
#             k0 += 1
#     print(k0 * k5 + k0 * k1 + k2 * k5)
from itertools import count

# 5
# with open("../Task files/27th files/27A_2723.txt") as file:
#     k19 = 0
#     n = int(file.readline())
#     for _ in range(n):
#         num = int(file.readline())
#         if num % 19 == 0:
#             k19 += 1
#     print(k19 * (k19 - 1) * (k19 - 2) // 6)
    # a = list(map(int, file))
    # cnt = 0
    # from itertools import combinations
    # for n1, n2, n3 in combinations(a, 3):
    #     if n1 % 19 == 0 and n2 % 19 == 0 and n3 % 19 == 0:
    #         cnt += 1
    # print(cnt)

# with open("../Task files/27th files/27B_2723.txt") as file:
#     k19 = 0
#     n = int(file.readline())
#     for _ in range(n):
#         num = int(file.readline())
#         if num % 19 == 0:
#             k19 += 1
#     print(k19 * (k19 - 1) * (k19 - 2) // 6)


# 6
# with open("../Task files/27th files/27A_2724.txt") as file:
#     k131 = 0
#     n = int(file.readline())
#     a = list(map(int, file))
#     from itertools import combinations
#     for n1, n2 in combinations(a, 2):
#         if (n1 + n2) % 131 == 0:
#             k131 += 1
#     print(k131)
#
# with open("../Task files/27th files/27B_2721.txt") as file:
#     '''1 sposob'''
#     # k131 = 0
#     # n = int(file.readline())
#     # a = list(map(int, file))
#     # from itertools import combinations
#     # for n1, n2 in combinations(a, 2):
#     #     if (n1 + n2) % 131 == 0:
#     #         k131 += 1
#     # print(k131)
#     '''2 sposob. smart'''
#     n = int(file.readline())
#     ost = [0]*131
#     for i in range(n):
#         num = int(file.readline())
#         ost[num % 131] += 1
#     cnt = 0
#     cnt += ost[0]*(ost[0] - 1) // 2
#     for i in range(1, 66):
#         cnt += ost[i] * ost[131 - i]
#     print(cnt)

# 7
# with open("../Task files/27th files/27A_2725.txt") as file:
#     n = int(file.readline())
#     ost = [0] * 69
#     for i in range(n):
#         num = int(file.readline())
#         ost[num % 69] += 1
#     cnt = 0
#     cnt += ost[0] * (ost[0] - 1) // 2
#     for i in range(1, 69):
#         cnt += ost[i] * (ost[i] - 1) // 2
#     print(cnt)
#
#
# with open("../Task files/27th files/27B_2725.txt") as file:
#     n = int(file.readline())
#     ost = [0] * 69
#     for i in range(n):
#         num = int(file.readline())
#         ost[num % 69] += 1
#     cnt = 0
#     cnt += ost[0] * (ost[0] - 1) // 2
#     for i in range(1, 69):
#         cnt += ost[i] * (ost[i] - 1) // 2
#     print(cnt)


# 8
# with open("../Task files/27th files/27A_2733.txt") as file:
#     n = int(file.readline())
#     a = list(map(int, file))
#     cnt = 0
#     from itertools import combinations
#     for n1, n2 in combinations(a, 2):
#         if (n1 > 50 * 10**3 or n2 > 50 * 10**3) and (n1 + n2) % 80 == 0:
#             cnt += 1
# print(cnt)

# with open("../Task files/27th files/27B_2733.txt") as file:
#     n = int(file.readline())
#     m50 = [0] * 80
#     l50 = [0] * 80
#     for _ in range(n):
#         num = int(file.readline())
#         if num > 50 * 10**3:
#             m50[num % 80] += 1
#         else:
#             l50[num % 80] += 1
#     cnt = 0
#     cnt += m50[0] * (m50[0] - 1) // 2 + m50[40] * (m50[40] - 1) // 2
#     for i in range(1, 40):
#         cnt += m50[i] * m50[80 - i]
#
#     cnt += m50[0] * l50[0] + m50[40] * l50[40]
#     for i in range(1, 40):
#         cnt += m50[i] * l50[80 - i]
#         cnt += l50[i] * m50[80 - i]
# print(cnt)

# 9
# with open("../Task files/27th files/27A_2737.txt") as file:
#     n = int(file.readline())
# #     a = list(map(int, file))
# #     cnt = 0
# #     from itertools import combinations
# #     for n1, n2 in combinations(a, 2):
# #         if (n1 + n2) == 2000:
# #             cnt += 1
# # print(cnt)
#
#     ost = [0] * 2000
#     for i in range(n):
#         num = int(file.readline())
#         if num < 2000:
#             ost[num] += 1
#     cnt = 0
#     cnt += ost[1000] * (ost[1000] - 1) // 2
#     for i in range(1, 1000):
#         cnt += ost[i] * ost[2000 - i]
#     print(cnt)
#
#
# with open("../Task files/27th files/27B_2737.txt") as file:
#     n = int(file.readline())
#     ost = [0] * 2000
#     for i in range(n):
#         num = int(file.readline())
#         if num < 2000:
#             ost[num] += 1
#     cnt = 0
#     cnt += ost[1000] * (ost[1000] - 1) // 2
#     for i in range(1, 1000):
#         cnt += ost[i] * ost[2000 - i]
#     print

# 10
# with open("../Task files/27th files/27A_2726.txt") as file:
#     n = int(file.readline())
#     mx_ch = 0
#     mx_nch = 0
#     for i in range(n):
#         num = int(file.readline())
#         if num % 2 == 0:
#             mx_ch = max(mx_ch, num)
#         elif num % 2 != 0:
#             mx_nch = max(mx_nch, num)
#     print(mx_ch + mx_nch)
#
# with open("../Task files/27th files/27B_2726.txt") as file:
#     n = int(file.readline())
#     mx_ch = 0
#     mx_nch = 0
#     for i in range(n):
#         num = int(file.readline())
#         if num % 2 == 0:
#             mx_ch = max(mx_ch, num)
#         elif num % 2 != 0:
#             mx_nch = max(mx_nch, num)
#     print(mx_ch + mx_nch)

# 11
# with open("../Task files/27th files/27A_2727.txt") as file:
#     n = int(file.readline())
#     mn = 10**11
#     mn31 = 10**11
#     for i in range(n):
#         num = int(file.readline())
#         if num % 31 == 0:
#             mn31 = min(num, mn31)
#         else:
#             mn = min(num, mn)
#     print(mn * mn31)
#
#
# with open("../Task files/27th files/27B_2727.txt") as file:
#     n = int(file.readline())
#     mn = 10**11
#     mn31 = 10**11
#     for i in range(n):
#         num = int(file.readline())
#         if num % 31 == 0:
#             mn31 = min(num, mn31)
#         else:
#             mn = min(num, mn)
#     print(mn * mn31)

# 12
# with open("../Task files/27th files/27A_2728.txt") as file:
#     n = int(file.readline())
#     mx23 = 0
#     mx_ch = 0
#     for i in range(n):
#         x = int(file.readline())
#         if x % 23 == 0:
#             mx23 = max(mx23, x)
#         if x % 2 == 0:
#             mx_ch = max(mx_ch, x)
#     print(mx23)
#     print(mx_ch)
#     print(mx23 + mx_ch)
# print()
# with open("../Task files/27th files/27B_2728.txt") as file:
#     n = int(file.readline())
#     mx23 = 0
#     mx_nch = 0
#     for i in range(n):
#         x = int(file.readline())
#         if x % 23 == 0:
#             mx23 = max(mx23, x)
#         if x % 2 == 1:
#             mx_ch = max(mx_ch, x)
#     print(mx23)
#     print(mx_ch)
#     print(mx23 + mx_ch)

# 13
# with open("../Task files/27th files/27A_2729.txt") as file:
#     n = int(file.readline())
#     a = list(map(int, file))
#     mn = 10**10
#     from itertools import combinations
#     for i in combinations(a, 3):
#         if sum(i) % 11 == 0:
#             mn = min(mn, sum(i))
#     print(mn)

# with open("../Task files/27th files/27B_2729.txt") as file:
#     n = int(file.readline())
#     mn = [[] for _ in range(11)]
#     for i in range(n):
#         x = int(file.readline())
#         mn[x % 11] += [x]
#     a = []
#     for i in range(11):
#         mn[i].sort()
#         a += mn[i][:3]
#     ans = []
#     from itertools import combinations
#     for i in combinations(a, 3):
#         i = list(i)
#         if sum(i) % 11 == 0:
#             ans += [sum(i)]
#     print(min(ans))

# dosrok
with open("Task files/27th files/27A_7603.txt") as file:
    n = int(file.readline())
    k = int(file.readline())
    print(k)
    j = 0
    arr = []
    for i in range(n):
        x = int(file.readline())
        arr.append([x, j])
        j += 1
    arr.sort(reverse=True)
    print(arr[:100])
    print(arr[0][0] + arr[1][0])
