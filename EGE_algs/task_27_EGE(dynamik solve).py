'''
file = [7, 3, 18, 5, 12, 15, 6, 7]

cnt = 0
n = len(file)
k15 = 0
k3 = 0
k5 = 0
for i in range(n):
    x = file[i]
    if x % 15 == 0:
        cnt += i
    elif x % 3 == 0:
        cnt += k5
    elif x % 5 == 0:
        cnt += k3
    else:
        cnt += k15

    if x % 15 == 0:
        k15 += 1
    if x % 3 == 0:
        k3 += 1
    if x % 5 == 0:
        k5 += 1
print(cnt)
'''


# 1
# with open("../Task files/27th files/27A_2720.txt") as f:
#     n = int(f.readline())
#     cnt = 0
#     k7 = 0
#     for i in range(n):
#         x = int(f.readline())
#         if x % 7 == 0:
#             cnt += i
#         else:
#             cnt += k7
#
#         if x % 7 == 0:
#             k7 += 1
#     print(cnt)

# with open("../Task files/27th files/27B_2720.txt") as f:
#     n = int(f.readline())
#     cnt = 0
#     k7 = 0
#     for i in range(n):
#         x = int(f.readline())
#         if x % 7 == 0:
#             cnt += i
#         else:
#             cnt += k7
#
#         if x % 7 == 0:
#             k7 += 1
#     print(cnt)

# 2
# for i in range(1, int(65 ** 0.5) + 1):
#     if 65 % i == 0:
#         print(i, 65//i, end=' ')
# 65 : 1 65 5 13
# with open("../Task files/27th files/27A_2721.txt") as file:
#     n = int(file.readline())
#     k5 = 0
#     k13 = 0
#     k65 = 0
#     cnt = 0
#     for i in range(n):
#         x = int(file.readline())
#         if x % 65 == 0:
#             cnt += i
#         elif x % 13 == 0:
#             cnt += k5
#         elif x % 5 == 0:
#             cnt += k13
#         else:
#             cnt += k65
#
#         if x % 5 == 0:
#             k5 += 1
#         if x % 13 == 0:
#             k13 += 1
#         if x % 65 == 0:
#             k65 += 1
# print(cnt)

# with open("../Task files/27th files/27A_2722.txt") as f:
#     n = int(f.readline())
#     k5, k0, k1, k2 = 0
#     cnt = 0
#     for i in range(n):
#         x = int(f.readline())
#         if x % 5 == 0 and x % 2 == 0:
#             k0 += 1
#         elif x % 5 == 0 and x % 2 != 0:
#             k5 += 1
#         elif x % 5 != 0 and x % 2 == 0:
#             k0 += 1
#         elif x % 5 != 0 and x % 2 != 0:
#             k0 += 1
#         else:
#             cnt += i
# 4
# with open("../Task files/27th files/27B_2724.txt") as f:
#     n = int(f.readline())
#     arr = [0]*131
#     cnt = 0
#     for i in range(n):
#         x = int(f.readline())
#         if x % 131 == 0:
#             ost = 0
#         else:
#             ost = 131 - x % 131
#
#         cnt += arr[ost]
#         arr[x % 131] += 1
#     print(cnt)

# with open("../Task files/27th files/27A_2724.txt") as f:
#     n = int(f.readline())
#     arr = [0]*131
#     cnt = 0
#     for i in range(n):
#         x = int(f.readline())
#         if x % 131 == 0:
#             ost = 0
#         else:
#             ost = 131 - x % 131
#
#         cnt += arr[ost]
#         arr[x % 131] += 1
# print(cnt)

# 5 кол-во чисел сумма которых кратна 80 и хотя бы одно из слагаемых > 50000
# with open("../Task files/27th files/27B_2733.txt") as f:
#     n = int(f.readline())
#     arr_more = [0]*80
#     arr_less = [0]*80
#     cnt = 0
#     for i in range(n):
#         x = int(f.readline())
#         if x > 50000:
#             ost = 0 if x % 80 == 0 else 80 - x % 80
#             cnt += arr_more[ost]
#             cnt += arr_less[ost]
#         else:
#             ost = 0 if x % 80 == 0 else 80 - x % 80
#             cnt += arr_more[ost]
#         if x > 50000:
#             arr_more[x % 80] += 1
#         else:
#             arr_less[x % 80] += 1
# print(cnt)

# 6 максимальная нечетная сумма
# н + ч = н
# with open("../Task files/27th files/27A_2726.txt") as f:
#     n = int(f.readline())
#     mx_sm = 0
#     arr = list(map(int, f))
#     arr.sort(reverse=True)
#     print(arr[0] + arr[1])


# with open("../Task files/27th files/27B_2726.txt") as f:
#     n = int(f.readline())
#     arr = list(map(int, f))
#     arr.sort(reverse=True)
#     print(arr[:100])

# 6 мин произведение пары кратное 31
# with open("../Task files/27th files/27B_2727.txt") as f:
#     n = int(f.readline())
#     mn_31 = float('inf')
#     mn = float('inf')
#     for i in range(n):
#         x = int(f.readline())
#         if x % 31 == 0:
#             mn_31 = min(mn_31, x)
#         else:
#             mn = min(mn, x)
#     print(mn, mn_31)
#     print(mn_31 * mn)

# 7 макс четн сумма пары причем хотя бы одно слагаемое кратно 23
# ч = н + н или ч = ч + ч
with open("Task files/27th files/27A_2728.txt") as f:
    n = int(f.readline())
#     mx23 = 0
#     mx = 0
#     mxs = 0
#
#     for i in range(n):
#         x = int(f.readline())
#
#         if (mxs + x) % 2 == 0:
#             if x % 23 == 0:
#                 mxs = max(x + mx, mxs)
#             else:
#                 mxs = max(x + mx23, mxs)
#         elif (mxs + x) % 2 != 0:
#             if x % 23 == 0:
#                 mxs = max(x + mx, mxs)
#             else:
#                 mxs = max(x + mx23, mxs)
#
#         mx = max(mx, x)
#         if x % 23 == 0:
#             mx23 = max(mx23, x)
# print(mxs)

