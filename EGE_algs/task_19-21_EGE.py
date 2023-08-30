'''
 задание 19-21 на сайте kompege.ru
 Стоит обратить внимание на строчку if h > 60: return 'p1' /
 эта штука нужна, из-за условия задачи, тк если игрок перевалиевает за 60 камней, то он проигрывает, и победитель - противник. => если ваня перевалтивает за 60, то он проиграл
'''

from functools import lru_cache
from sys import setrecursionlimit
setrecursionlimit(10**6)
#
#
# def move(h):
#     return h + 1, h * 2, h * 3
#
#
# @lru_cache(None)
# def game(h):
#     if 36 <= h <= 60:
#         return 'w'
#     if h > 60:
#         return 'p1'
#     if any(game(i) == 'w' for i in move(h)):
#         return 'p1'
#     if all(game(i) == 'p1' for i in move(h)):
#         return 'v1'
#     if any(game(i) == 'v1' for i in move(h)):
#         return 'p2'
#     if all(game(i) == 'p2' or game(i) == 'p1' for i in move(h)):
#         return 'v2'
#
#
# for s in range(1, 35 + 1):
#     if game(s) == 'v2':
#         print(s, game(s))

'''
задания 19-21 с сайта kompege.ru/
задача с несколькими кучами
'''
#
# from functools import lru_cache
#
#
# def move(h):
#     a, b = h
#     return (a + 1, b), (a * 2, b), (a, b + 1), (a, b * 2)
#
#
# @lru_cache(None)
# def game(h):
#     a, b = h
#     if a + b >= 59:
#         return 'w'
#     if any(game(i) == 'w' for i in move(h)):
#         return 'p1'
#     if all(game(i) == 'p1' for i in move(h)):
#         return 'v1'
#     if any(game(i) == 'v1' for i in move(h)):
#         return 'p2'
#     if all(game(i) == 'p1' or game(i) == 'p2' for i in move(h)):
#         return 'v2'
#
#
# for s in range(1, 53):
#     h = 5, s
#     if game(h) == 'p1':
#         print(s, game(h))
#
# уменьшение камней
def move(h):
    a, b = h
    return (a - 1, b), (a // 2 if a % 2 == 0 else a // 2 + a % 2, b), (a, b - 1), (a, b // 2 if b % 2 == 0 else b % 2 + b // 2)

@lru_cache(None)
def game(h):
    a, b = h
    if a + b <= 20: return 'w'
    if any(game(i) == 'w' for i in move(h)): return 'p1'
    if all(game(i) == 'p1' for i in move(h)): return 'v1'
    if any(game(i) == 'v1' for i in move(h)): return 'p2'
    if all(game(i) == 'p1' or game(i) == 'p2' for i in move(h)): return 'v2'


for s in range(11, 22):
    h = 10, s
    print(s, game(h))
    if game(h) == 'v1':
        print(s, game(h))

# def move(h):
#     return h+1, h*3
#
#
# @lru_cache(None)
# def game(h):
#     if h >= 2163: return 'w'
#     if any(game(i) == 'w' for i in move(h)): return 'p1'
#     if all(game(i) == 'p1' for i in move(h)): return 'v1'
#     if any(game(i) == 'v1' for i in move(h)): return 'p2'
#     if all(game(i) == 'p1' or game(i) == 'p2' for i in move(h)): return 'v2'
#
#
# for s in range(2162, 1, -1):
#     if game(s) == 'v2':
#         print(s, game(s))
