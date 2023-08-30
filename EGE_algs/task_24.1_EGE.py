# kompege
# 1
# st = open("Task files/24.2.txt").readline()
# # print(st)
# while 'XVIII' in st:
#     st = st.replace('XVIII', ' # ')
# st = st.split()
# print(st)
# cnt = 0
# for i in st:
#     if i == '#':
#         cnt += 1
# print(cnt)
# 2
# s = open("Task files/24.2.txt").readline()
# while 'TIK' in s or 'TOK' in s:
#     if 'TIK' in s:
#         s = s.replace('TIK', ' # ')
#     else:
#         s = s.replace('TOK', ' # ')
# s = s.split()
# cnt = 0
# for i in s:
#     if i == '#':
#         cnt += 1
# print(cnt)
# 3
# s = open("Task files/24.2.txt").readline()
# while 'STOCK' in s:
#     s = s.replace('STOCK', ' ')
# while 'OCK' in s:
#     s = s.replace('OCK', ' # ')
# s = s.split()
# print(s.count('#'))
# 4
# s = open("Task files/BOSS.txt").readline()
# while 'JBOSSJBOSSJ' in s:
#     s = s.replace('JBOSSJBOSSJ', 'JBOSSJ JBOSSJ')
# # print(s)
# while 'JBOSS' in s or 'BOSSJ' in s or 'JBOSSJ' in s:
#     if 'JBOSS' in s:
#         s = s.replace('JBOSS', ' ')
#     if 'BOSSJ' in s:
#         s = s.replace('BOSSJ', ' ')
#     if 'JBOSSJ' in s:
#         s = s.replace('JBOSSJ', ' ')
# print(s.count(' '))
# while 'BOSS' in s:
#     s = s.replace('BOSS', ' # ')
# s = s.split()
# # print(s)
# print(s.count('#'))
#

''''''
# while 'JBOSSJBOSSJ' in s: s = s.replace('JBOSSJBOSSJ', 'JBOSSJ JBOSSJ')
# print(s.count('BOSS') - (s.count('JBOSS') + s.count('BOSSJ') - s.count('JBOSSJ')))
''''''

# 5
# s = open("Task files/24.2.txt").readline()
# while 'XIXIX' in s: s = s.replace('XIXIX', 'XIX XIX')
# while 'XIX' in s: s = s.replace('XIX', ' # ')
# print(s.count('#'))
# 6
# s = open("Task files/24(20 kompege).txt").readline()
# while 'XXXXX' in s:
#     s = s.replace('XXXXX', 'XXXX XXXX')
# while 'XXXX' in s:
#     s = s.replace('XXXX', ' # ')
# print(s.count('#'))
# 7
# s = open("Task files/24(20 kompege).txt").readline()
# cnt = 0
# print(s)
# for i in range(1, len(s) - 2):
#     if s[i - 1] == 'G' and s[i+1] == 'M' and s[i+2] == 'E':
#         cnt += 1
# print(cnt)
# 8
# s = open("Task files/24(20 kompege).txt").readline()
# cnt = 0
# for i in range(len(s) - 4):
#     if s[i] == 'A' and s[i + 2] == 'A' and s[i + 4] == 'A':
#         cnt += 1
# print(cnt)
# 9
# s = open("Task files/24(20 kompege).txt").readlines()
# cnt = 0
# for i in s:
#     if i.count('S') == i.count('X'):
#         cnt += 1
# print(cnt)
# 10
# s = open("Task files/24(20 kompege).txt").readlines()
# cnt = 0
# for i in s:
#     b = i.count('B')/len(i)
#     a = i.count('A')/len(i)
#     # print(b, a)
#     if b/a >= 1.05:
#         cnt += 1
# print(cnt)
#  11
# s = open("Task files/24(20 kompege).txt").readlines()
# cnt = 0
# for i in s:
#     for j in range(len(i) - 3):
#         if i[j] == 'K' and i[j+2] == 'G' and i[j+3] == 'E':
#             cnt += 1
#             break
# print(cnt)
# 12
# s = open("Task files/24(20 kompege).txt").readlines()
# cnt = 0
# for i in s:
#     while 'AOAO' in i: i = i.replace('AOAO', 'AOA OAO')
# for i in s:
#     if i.count('AOA') > i.count('OAO'):
#         cnt += 1
# print(cnt)
# 14
# ABOBA - example
# s = open("Task files/24(20 kompege).txt").readline()
# cnt = 0
# for i in range(len(s) - 5):
#     if s[i] == s[i + 4] and s[i + 1] == s[i + 3]:
#         cnt += 1
# print(cnt)
# 15
# s = open("Task files/24(20 kompege).txt").readline().strip()
# d = {l: s.count(l) for l in sorted(set(s))}
# m = 0
# mk = ''
# for k, v in d.items():
#     if v > m:
#         m = v
#         mk = k
# # print(*d.items())
# print(mk, m)
# 16
# s = open("Task files/24(20 kompege).txt").readline().strip()
# d = {letter: s.count(letter) for letter in sorted(set(s))}
# print(d)
# mx = 0
# mn = 10**6
# smx = ''
# smn = ''
# for k, v in d.items():
#     if v > mx:
#         mx = v
#         smx = k
#     if v < mn:
#         mn = v
#         smn = k
# print(mx, smx)
# print(mn, smn)
# print(mx - mn)
# 17
# s = open("Task files/24(20 kompege).txt").readline().strip()
#
#
# def c(l):
#     cnt = 0
#     for i in range(len(s) - 2):
#         if s[i] == s[i+2] and s[i+1] == l:
#             cnt += 1
#     return cnt
#
#
# d = {letter: c(letter) for letter in sorted(set(s))}
# mx = 0
# st = ''
# for k, v in d.items():
#     if v > mx:
#         mx = v
#         st = k
# print(st, mx)
# 18
# s = open("Task files/24(20 kompege).txt").readline().strip()
#
#
# def c(n):
#     cnt = 0
#     for i in range(len(s) - 4):
#         if (s[i] + s[i+1]) == 'CB' and (s[i + 3] + s[i + 4]) == 'BC' and s[i + 2] == n:
#             cnt += 1
#     return cnt
#
#
# d = {letter: c(letter) for letter in sorted(set(s))}
# mn = 0
# st = ''
# for k, v in d.items():
#     if v > mn:
#         mn = v
#         st = k
# print(st, mn)
#
# 19
# file = open("Task files/24 (19kompege).txt").readlines()
# # print(len(file))
# dictq = {f"array number {arr}": file[arr].count('Q') for arr in range(len(file)-1, 0, -1)}
# # print(dictq)
# mx = 0
# smx = ''
# for k, v in dictq.items():
#     if v > mx:
#         mx = v
#         smx = k
# # print(smx, mx)
# n = int(smx.lstrip('array number'))
# ar = file[n].strip()
# rare = {letter: ar.count(letter) for letter in ar}
# # print(rare)
# mn = 10**6
# smn = ''
# for k, v in rare.items():
#     if v < mn:
#         mn = v
#         smn = k
# # print(smn, mn)
# qnt = 0
# for ar in file:
#     qnt += ar.count(smn)
# print(smn + str(qnt))
#
# 20
# s = open("Task files/24(20 kompege).txt").readlines()
# Mx = 0
# l = ''
# for line in open("Task files/24(20 kompege).txt"):
#     cnt = 1
#     mx = 0
#     for i in range(len(line) - 1):
#         if line[i] == line[i + 1]:
#             cnt += 1
#             if cnt > mx:
#                 mx = cnt
#         else:
#             cnt = 1
#     if Mx < mx:
#         l = line.rstrip()
#         Mx = mx
# # print(l)
# d = {letter: l.count(letter) for letter in sorted(set(l))}
# # print(d)
# let = ''.join([i for i in d if d[i] == max(d.values())])
# print(let)
# qnt = 0
# for i in open("Task files/24(20 kompege).txt"):
#     qnt += i.count(let)
# print(let + str(qnt))
# print(similar('X', 'XXXXAAXXXXXXXX'))
#
# st = open("Task files/24.s.txt").readline()
# ans = []
# cnt = 1 ## тк у нас уже имеется один список
# for i in range(1, len(st)):
#     if st[i-1] != st[i]:
#         cnt += 1
#     else:
#         ans.append(cnt)
#         cnt = 1
# print(max(ans))

# 19
# s = open("../Task files/24.txt").readline().strip()
# s = s.replace('BA', 'F')
# s = s.replace('CA', 'F')
# s = s.replace('DA', 'F')
# s = s.replace('BO', 'F')
# s = s.replace('CO', 'F')
# s = s.replace('DO', 'F')
# # print(s)
# for i in range(len(s)):
#     if 'F'*i in s:
#         print(i)

# 20
# s = open("../Task files/24.txt").readline().strip()
# s = s.replace('A1', '#')
# s = s.replace('A2', '#')
# s = s.replace('B1', '#')
# s = s.replace('B2', '#')
# for i in range(len(s)):
#     if '#'*i in s:
#         print(i)

# 21
# s = open("../Task files/24.txt").readline().strip()
# while 'NPO' in s: s = s.replace('NPO', '#')
# while 'PNO' in s: s = s.replace('PNO', '#')
# # print(s)
# for i in range(len(s)):
#     if '#'*i in s:
#         print(i)

# 22
# s = open("../Task files/24.txt").readline().strip()
# s = s.replace('11A', '#')
# s = s.replace('12A', '#')
# s = s.replace('21A', '#')
# s = s.replace('22A', '#')
# s = s.replace('11B', '#')
# s = s.replace('12B', '#')
# s = s.replace('21B', '#')
# s = s.replace('22B', '#')
# for i in range(len(s)):
#     if '#'*i in s:
#         print(i)

# 23
# from fnmatch import fnmatch
# cnt = 0
# s = open("../Task files/24.txt").readline().strip()
# for i in range(0, len(s), 3):
#     if fnmatch(s[i]+s[i+1]+s[i+2], 'A*A') or fnmatch(s[i]+s[i+1]+s[i+2], 'C*C'):
#         cnt += 1
# print(cnt)
# wrong

# 24
# s = open("../Task files/24.1.txt").readline().strip()
# # print(s)
# while 'CA' in s:s = s.replace('CA', '#')
# for i in range(len(s)):
#     if "#"*i in s:
#         print(i)
