'''https://inf-ege.sdamgia.ru/problem?id=38604'''
# with open(r"C:\Users\1234x\PycharmProjects\Tests and practice\Task files\27th files\27_B(1).txt") as file:
#     n = int(file.readline())
#     k = 43
#     mxs = 0
#     sm = 0
#     minL = 0
#     l = 0
#     poverka = 0
#     ost = [10**11 for _ in range(43)]
#     lens = [0 for _ in range(43)]
#     for i in range(n):
#         x = int(file.readline())
#         sm += x
#         div = sm % k
#         if div == 0:
#             mxs = sm
#             minL = i
#         else:
#             proverka = sm - ost[div]
#             l = i - lens[div]
#             if proverka > mxs:
#                 mxs = proverka
#                 minL = l
#             if proverka == mxs and l < minL:
#                 mxs = proverka
#                 minL = l
#             if sm < ost[div]:
#                 ost[div] = sm
#                 lens[div] = i
#     print(minL)

# '''https://inf-ege.sdamgia.ru/problem?id=47024'''
# with open("27kfu/27-B(2).txt") as f:
#     n = int(f.readline())
#     ost = [0]*1111
#     cnt = 0
#     sm = 0
#     for i in range(n):
#         x = int(f.readline())
#         sm += x
#         if sm % 1111 == 0:
#             cnt += 1
#         cnt += ost[sm % 1111]
#         ost[sm % 1111] += 1
#     print(cnt)

# 19 var krylov
# with open("../Task files/27th files/27v19_A.txt") as f:
#     sm = 0
#     n = int(f.readline())
#     array = []
#     for i in range(n):
#         x = list(map(int, f.readline().split()))
#         array.append(x)
#         if (sm + min(x)) % 51 != 0:
#             sm += min(x)
#         elif (sm + min(x)) % 51 == 0 and (sm + max(x)) % 51 != 0:
#             sm += max(x)
#         elif (sm + min(x)) % 51 == 0 and (sm + max(x)) % 51 == 0:
#             sm += min(x)
#     print(sm)

    # array.sort(reverse=True)
    # print(array[0])
# 352300 A
# 332620623 B -


# with open('../Task files/27th files/27v19_B.txt') as f:
#     sm = 0
#     n = int(f.readline())
#     for i in range(n):
#         x = list(map(int, f.readline().split())).sort()
#         sm += x[0]
#

# with open('../Task files/27th files/27_A.txt') as file:
#     n = int(file.readline())
#     points = []
#     for i in file:
#         dist, prob = map(int, i.split())
#         if prob % 36 == 0:
#             cont = prob // 36
#         else:
#             cont = prob // 36 + 1
#         points.append([dist, cont])
#     sm = 0
#     # deliver = []
#     mx = 10**9
#     for i in range(n):
#         for j in range(n):
#             sm += points[j][1]*(abs(points[j][0] - points[i][0]))
#         mx = min(sm, mx)
#         sm = 0
#     print(mx)

# with open('../Task files/27th files/27_B.txt') as file:
#     n = int(file.readline())
#     points = []
#     for i in file:
#         dist, prob = map(int, i.split())
#         if prob % 36 == 0:
#             cont = prob // 36
#         else:
#             cont = prob // 36 + 1
#         points.append([dist, cont])
#     cost = 0
#     right = 0
#     for i in range(1, n):
#         cost += points[i][1]*(abs(points[i][0] - points[0][0]))
#         right += points[i][1]
#     left = 0
#     cost_mn = cost
#     for i in range(1, n):
#         left += points[i-1][1]
#         cost_mn = min(cost_mn, cost_mn - right * (points[i][0] - points[i-1][0]) + left * (points[i][0] - points[i-1][0]))
#         right -= points[i-1][1]
#     print(cost_mn)

# with open("../Task files/27th files/107_27_B.txt") as file:
#     n = int(file.readline())
#     way = []
#     j = 1
#     for i in file:
#         dist, trash = j, int(i)
#         way.append([dist, trash])
#         j += 1
#     cost = 0
#     right = 0
#     for i in range(1, n):
#         cost += way[i][1] * (abs(way[i][0] - way[0][0]))
#         right += way[i][1]
#     left = 0
#     cost_mn = cost
#     for i in range(1, n):
#         left += way[i-1][1]
#         cost_mn = min(cost_mn, cost_mn - right * (way[i][0] - way[i-1][0]) + left * (way[i][0] - way[i-1][0]))
#         right -= way[i-1][1]
#     print(cost_mn)

#->4 5 | 0 1 2 | 3 | 4 5->
# кольцевая автодорога
'''На каждом 3-м километре кольцевой автодороги с двусторонним движением установлены контейнеры для мусора.
Длина кольцевой автодороги равна 3N километров.
 Нулевой километр и 3N-й километр автодороги находятся в одной точке.
 Известно количество мусора, которое накапливается ежедневно в каждом из контейнеров. 
Из каждого пункта мусор вывозит отдельный мусоровоз.
 Стоимость доставки мусора вычисляется как произведение количества мусора на расстояние от пункта до центра переработки.
 Центр переработки отходов открыли в одном из пунктов сбора мусора таким образом,
 чтобы общая стоимость доставки мусора из всех пунктов в этот центр была минимальной.
Определите минимальные расходы на доставку мусора в центр переработки отходов'''
# with open("../Task files/27th files/107_27_B.txt") as f:
#     n = int(f.readline())
#     points = [3*int(s) for s in f]
#     zero_cost = 0
#     right = 0
#     left = 0
#     cost = []
#     for i in range(1, n//2):
#         zero_cost += (points[i] + points[n - i]) * i
#         right += points[i]
#         left += points[n-i]
#     zero_cost += n//2 * points[n//2]
#     cost.append(zero_cost)
#     for i in range(1, n):
#         cost.append(cost[-1] + left + points[i-1] - right - points[(i + (n//2) - 1) % n])
#         right = right - points[i] + points[(i + (n // 2) - 1) % n]
#         left = left + points[i - 1] - points[(i + (n // 2)) % n]
# print(min(cost))


# прямая автодорога. идея - движ окно. м - допустимое расстояние перемещения
# 27
# perebor
# with open(r"C:\Users\1234x\Downloads\27_A_7275_OPENFIPI.txt") as file:
#     n, m = map(int, file.readline().split())
#     way = []
#     for i in file:
#         point, prob = map(int, i.split())
#         way.append([point, prob//30 if prob%30==0 else prob//30+1])
#
#     max_cnt = 0
#     for i in range(n):
#         count = 0
#         for j in range(n):
#             dist = abs(way[i][0] - way[j][0])
#             if dist <= m:
#                 count += way[j][1]
#         max_cnt = max(max_cnt, count)
#     print(max_cnt)

# effectivity
# with open(r"C:\Users\1234x\Downloads\27_B_7275_OPENFIPI.txt") as file:
#     n, m  = map(int, file.readline().split())
#     way = [0]*10**7
#     for i in file:
#         point, prob = map(int, i.split())
#         way[point] = prob//30 if prob%30==0 else prob//30+1
#     max_cnt = cnt = sum(way[:2*m+1])
#     if way[m] != 0:
#         max_cnt = cnt
#
#     for i in range(1, len(way)-2*m):
#         cnt = cnt - way[i-1] + way[i+2*m]
#     if way[i+m] != 0:
#         max_cnt = max(cnt, max_cnt)
# print(max_cnt)