'''https://www.youtube.com/watch?v=E9ZyTub3i9g&list=PLwqOjxukojIlfQZwJGQDJ5mMab9xNRqGu'''
# Демоверсия 2021, kompege
# не метод частичных сумм
# with open("../Task files/27_KOPMEGE/27-B_23.txt") as file:
#     n = int(file.readline())
#     k = 3 # число на которое не должна делится сумма
#     arr = []
#     for i in file:
#         a, b = map(int, i.split())
#         arr.append([a, b])
#     max_sum = 0
#     difference = float('inf') # разность
#     for i in range(n):
#         a, b = arr[i]
#         max_sum += max(a, b)
#         if a %k != b % k:
#             difference = min(difference, abs(a -b))
#     if max_sum % k == 0:
#         print(max_sum - difference)
#     else:
#         print(max_sum)

# Апробация 27.04, 1208
# 3ки чисел!
# with open("../Task files/27_KOPMEGE/27_B_1208.txt") as file:
#     n = int(file.readline())
#     k = 103
#     arr = []
#     for i in file:
#         a, b, c = map(int, i.split())
#         arr.append([a, b, c])
#
#     diff = float('inf')
#     sm = 0
#     for i in range(n):
#         a, b, c = arr[i]
#         sm += max(a, b, c)
#         if a % k != b % k:
#             diff = min(diff, abs(a - b))
#         if a % k != c % k:
#             diff = min(diff, abs(a - c))
#         if b % k != c % k:
#             diff = min(diff, abs(b - c))
#     if sm % k == 0:
#         print(sm - diff)
#     else:
#         print(sm)

# Основная волна 2021
# префиксные суммы
'''Будем последовательно считывать числа из файла, суммируя все полученные числа.
 В массиве mins будем накапливать суммы с остатками от 0 до 42,
 в массиве minl будем накапливать длины для этих сумм. 
Каждую итерацию цикла будем проверять, делится ли текущая сумма на 43 без остатка.
 Если текущая сумма делится на 43 с определённым остатком,
 будем вычитать из неё сумму с таким же остатком из массива mins и
 записывать полученное значение в переменную maxsum
 (если полученная сумма будет больше текущего значения переменной),
 то же самое будем проделывать для минимальной длины последовательности.'''
# with open("../Task files/27_KOPMEGE/27_B_1869.txt") as file:
#     n = int(file.readline())
#     k = 89
#     sm = mx_sm = l = 0
#     prefix = [float('inf')]*k
#     leng = [0]*k
#     for i in range(n):
#         sm += int(file.readline())
#         if sm % k == 0 and sm > mx_sm:
#             l = i + 1
#             mx_sm = sm
#         if (sm - prefix[sm%k] > mx_sm) or ((sm - prefix[sm%k] == mx_sm) and (i - leng[sm%k]) < l):
#             mx_sm = sm - prefix[sm % k]
#             l = i - leng[sm % k]
#         if prefix[sm % k] > sm:
#             prefix[sm % k] = sm
#             leng[sm % k] = i
#     print(l)

'''https://inf-ege.sdamgia.ru/problem?id=47024'''
'''Если будет найдена подпоследовательность чисел с остатком от деления суммы элементов этой подпоследовательности на 1111 равным 1,
 чтобы сумма элементов найденной подпоследовательности была кратна 1111,
 достаточно вычесть из неё сумму элементов другой подпоследовательности с остатком 1.
 Объявим массив lefts, в котором будем хранить количество найденных подпоследовательностей
 с остатком от деления суммы элементов этой подпоследовательности на 1111 от 0 до 1110. Каждый раз, 
находя подпоследовательность с тем или иным остатком от деления суммы элементов этой подпоследовательности на 1111,
 будем прибавлять к переменной count хранящееся
 в массиве lefts значение с соответствующим остатком от деления суммы элементов этой подпоследовательности.
 '''
# сумма кратная k
# f = open("27-B.txt")
# n = int(f.readline())
# lefts = [0 for i in range(1111)]
# count = 0
# sumi = 0
# for i in range(1, n + 1):
#     num = int(f.readline())
#     sumi += num
#     if sumi % 1111 == 0:
#         count = count + 1
#     count += lefts[sumi % 1111]
#     lefts[sumi % 1111] += 1
# print(count)

# кольцевая дорога
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
#     zero_cost = right = lefts = 0
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

# Прямая магистраль. мусорки
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

# прямая магистраль, пробирки, движ окно
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
