from functools import lru_cache


# 1 - 3 variant from kfu
# 1 - v1 ,  2 - p1 , 3 - v2
# def move(h):
#     return h + 1, h * 3
#
#
# @lru_cache(None)
# def game(h):
#     if h >= 64:
#         return 'w'
#     if any(game(i) == 'w' for i in move(h)):
#         return 'p1'
#     if all(game(i) == 'p1' for i in move(h)):
#         return 'v1'
#     if any(game(i) == 'v1' for i in move(h)):
#         return 'p2'
#     if all(game(i) == 'p1' or game(i) == 'p2' for i in move(h)):
#         return 'v2'
# #
#
# for s in range(1, 64):
#     if game(s) == 'v2':
#         print(s, game(s))

# 4 - 6 задача с условиями по ходам
# 1 - p2, 2 - v2, 3 - p3
# def move(h):
#     return h + 1, h + 2, h * 2
#
#
# # print(move(8))
#
#
# @lru_cache(None)
# def game(h):
#     if h >= 21:
#         return 'w'
#     if any(game(i) == 'w' for i in move(h)):
#         return 'p1'
#     if all(game(i) == 'p1' for i in move(h)):
#         return 'v1'
#     if any(game(i) == 'v1' for i in move(h)):
#         return 'p2'
#     if all(game(i) == 'p1' or game(i) == 'p2' for i in move(h)):
#         return 'v2'
#     if any(game(i) == 'v1' or game(i) == 'v2' for i in move(h)):
#         return 'p3'

#
# for s in range(1, 21):
#     if game(s) == 'p3':
#         print(s, game(s))

# 7 - 9
# 1 - v1 + неудачный ход петра, 2 - p2, 3 - v2
def move(h):
    a, b = h
    return (a + 1, b), (a * 2, b), (a, b + 1), (a, b * 2)


@lru_cache(None)
def game(h):
    a, b = h
    if a + b >= 255:
        return 'w'
    if any(game(i) == 'w' for i in move(h)):
        return 'p1'
    if any(game(i) == 'p1' for i in move(h)):
        return 'v1'
    if any(game(i) == 'v1' for i in move(h)):
        return 'p2'
    if all(game(i) == 'p1' or game(i) == 'p2' for i in move(h)):
        return 'v2'


for s in range(1, 238):
    h = 17, s
    # print(s, game(h))
    if game(h) == 'v1':
        print(s, game(h))
# kod musy
# def m(h):
#     a, b = h
#     return (a * 2, b), (a, b + 1), (a + 1, b), (a, b * 2)
#
#
# @lru_cache(None)
# def g(h):
#     a, b = h
#     if a + b >= 255: return 'w'
#     if any(g(i) == 'w' for i in m(h)): return 'p1'
#     if any(g(i) == 'p1' for i in m(h)): return 'v1'
#     if any(g(i) == 'v1' for i in m(h)): return 'p2'
#     if all(g(i) == 'p1' or g(i) == 'p2' for i in m(h)): return 'v2'
#
#
# for b in range(1, 237 + 1):
#     h = 17, b
#     if g(h) == 'v1':
#         print(g(h), b)

# new егэ 2022
# def move(h):
#     a, b = h
#     return (a+1, b), (a, b+1), (a*2, b), (a, b*2)
#
#
# @lru_cache(None)
# def game(h):
#     a, b = h
#     if a + b >= 259: return 'w'
#     if any(game(i) == 'w' for i in  move(h)): return 'p1'
#     if all(game(i) == 'p1' for i in move(h)): return 'v1'
#     if any(game(i) == 'v1' for i in move(h)): return 'p2'
#     if all(game(i) == 'p1' or game(i) == 'p2' for i in move(h)): return 'v2'
#
#
# for s in range(1, 241):
#     h = 17, s
#     if game(h) == 'v2':
#         print(s, game(h))
# 1 - 61, 2 - 112 120, 3 - 111

# page 118
# def move(h):
#     a, b = h
#     return (a+2, b), (a, b + 2), (a * 2, b), (a, b * 2)
#
#
# @lru_cache(None)
# def game(h):
#     a, b = h
#     if a + b >= 142: return 'w'
#     if any(game(i) == 'w' for i in move(h)): return 'p1'
#     if all(game(i) == 'p1' for i in move(h)): return 'v1'
#     if any(game(i) == 'v1' for i in move(h)): return 'p2'
#     if all(game(i) == 'p1' or game(i) == 'p2' for i in move(h)): return 'v2'
#
#
# for s in range(1, 139):
#     h = 2, s
#     if game(h) == 'v2':
#         print(s, game(h))
# 1 - 35, 2 - 67 68, 3 - 66
