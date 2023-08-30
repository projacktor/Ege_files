# arr = [int(n) for n in open("Task files/17.txt")]
# ans = []

# Arsen 18 kompege.ru
# for i in range(len(arr) - 2):
#     if (arr[i] < 0 and str(arr[i])[-1] != '9') and\
#             (arr[i + 2] < 0 and str(arr[i + 2])[-1] != '9')\
#             and (arr[i + 1] > 0 and str(arr[i + 1])[-1] == '9'):
#         ans.append(arr[i] + arr[i + 1] + arr[i + 2])
#
# print(len(ans), max(ans))

# Kabanov 18
# for i in range(len(arr) - 2):
#     if not(arr[i] > 0 and str(arr[i])[-1] == '9') and\
#             not(arr[i + 2] > 0 and str(arr[i + 2])[-1] == '9')\
#             and (arr[i + 1] > 0 and str(arr[i + 1])[-1] == '9'):
#         ans.append(arr[i] + arr[i + 1] + arr[i + 2])
#
# print(len(ans), max(ans))

# a = [int(n) for n in open("../Task files/17(20t).txt")]
# ans = []
# thrfv = []

# for i in range(len(a)):
#     if a[i] % 35 == 0:
#         thrfv.append(sum(map(int, str(a[i]))))
# summa = sum(thrfv)
# print(summa)
#
#
# def hexagon(n):
#     h = hex(n)[2:]
#     if h[-2:] == 'ef':
#         return True
#     else:
#         return False


# ans2 = []
# # hexagon(233137)
# for i in range(len(a)-1):
#     if hexagon(a[i+1]) and a[i] > summa:
#         print(a[i], a[i+1])


# for i in range(len(a) - 1):
#     if (a[i] > summa and a[i+1] < summa and hexagon(a[i+1]) and not(hexagon(a[i]))) or\
#             (a[i+1] > summa and a[i] < summa and hexagon(a[i]) and not(hexagon(a[i+1]))):
#         # print(a[i], a[i+1])
#         ans.append(a[i] + a[i+1])
#
# print(len(ans), min(ans))

# 1
'''ar = list(map(int, open("Task files/17.1d.txt")))
ans =  []


def seven(n, m):
    if (str(n)[-1] == '7' and abs(n) % 10 == 7) and (str(m)[-1] != '7' and abs(m) != 7):
        return True
    if (str(m)[-1] == '7' and abs(m) % 10 == 7) and (str(n)[-1] != '7' and abs(n) != 7):
        return True
    if (str(n)[-1] != '7' and abs(n) % 10 != 7) and (str(m)[-1] != '7' and abs(m) != 7):
        return False


s = []
for i in range(len(ar)):
    if abs(ar[i]) % 10 == 7 and str(ar[i])[-1] == '7':
        s.append(ar[i])
mn7 = min(s)

for i in range(len(ar) - 1):
    if seven(ar[i], ar[i+1]) and (ar[i]*ar[i] + ar[i+1]*ar[i+1]) < mn7*mn7:
        ans.append(ar[i]*ar[i] + ar[i+1]*ar[i+1])
        print(ar[i], ar[i+1])
print(len(ans), max(ans))'''
# 671 96731834

# 2
'''ar = list(map(int, open("Task files/17.d2.txt")))
ans = []
nechet = []
for i in range(len(ar)):
    if ar[i] % 2 != 0:
        nechet.append(ar[i])
avg = sum(nechet) / len(nechet)


def tof(n, m):
    if (n % 5 == 0) and m < avg:
        return True
    if (m % 5 == 0) and n < avg:
        return True
    else: return False


for i in range(len(ar) - 1):
    if tof(ar[i], ar[i+1]):
        ans.append(ar[i] + ar[i + 1])
print(len(ans), max(ans))'''
# 1061 14847

# 3
'''ar = list(map(int, open("Task files/17.d3.txt")))
ans = []

mn = min(ar)
# print(mn)
for i in range(len(ar) - 1):
    if ar[i] % 117 == mn or ar[i + 1] % 117 == mn:
        ans.append(ar[i] + ar[i + 1])
print(len(ans), max(ans))'''
# 15067 199479

# 4
'''ar = [int(x) for x in open("Task files/17.d4.txt")]
# print(len(ar))
ans = []
avg = (max(ar) + min(ar)) / 2
mr = []
mr.append([ar[0], ar[-1]])
for i in range(1, len(ar) // 2 + 1):
    mr.append([ar[i], ar[(i+1) * -1]])


def tof(arr):
    if arr[0] > avg and arr[1] < avg: return True
    if arr[0] < avg and arr[1] > avg: return True
    else: return False


for a in mr:
    if tof(a):
        ans.append(sum(a))
print(len(ans), max(ans))'''
# 2120 14972