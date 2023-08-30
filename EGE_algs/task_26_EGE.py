# special
# задача про хранение багажа.
# Нужно узнать сколько чемоданов смогли упаковать
# и в какую ячейку был закинут последний
# смена места через мин
# with open("../Task files/26__.txt") as file:
#     n, k = map(int, file.readline().split())
#     # print(n, k)
#     bagazh = []
#     yacheyka = [0] * k
#     for s in file:
#         start, finish = map(int, s.split())
#         bagazh.append([start, finish])
#     cnt = 0
#     last = 0
#     bagazh.sort()
#     for i in range(n):
#         for j in range(k):
#             if yacheyka[j] == 0:
#                 yacheyka[j] = bagazh[i]
#                 cnt += 1
#                 last = 1 + j
#                 break
#             elif yacheyka[j][1] + 1 <= bagazh[i][0]:
#                 yacheyka[j] = bagazh[i]
#                 cnt += 1
#                 last = 1 + j
#                 break
# print(cnt, last)

"""--------------------------------------------------------------------"""

# special - двойная очередь
# задача с парковочными местами для автомобилей и микроавтобусов
# нужно найти сколько легковых смогут парокнутся и сколько всего машин не смогут.
# смена места моментальная
# with open("../Task files/26-statgrad.txt") as file:
#     n = int(file.readline()) # всего тачек
#     L = 80 # парковочные только для легковых
#     M = 20 # парковочные для автобусов или легковых
#     smog = 0
#     net = 0
#     cars = []
#     for i in file:
#         time, dur, clas = i.split()
#         cars.append([int(time), int(dur) + int(time), clas])
#     cars.sort()
#     # print(cars)
#     #0...L-1 мест для легковых, а след L...L+М места для микроавт
#     park = [0] * (L+M)
#     for i in range(n):
#         time, dur, clas = cars[i]
#         if clas == 'A':
#             for j in range(L + M):
#                 if park[j] <= time:
#                     park[j] = dur
#                     smog += 1
#                     break
#             else: # ВАЖНО! else относится к for, а не условию. срабатывает когда цикл завершился без break-ов
#                 net += 1
#         else:
#             for j in range(L, M+L):
#                 if park[j] <= time:
#                     park[j] = dur
#                     break
#             else:
#                 net += 1
# print(smog, net)
