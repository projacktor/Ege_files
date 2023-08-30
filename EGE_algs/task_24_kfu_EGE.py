
# 1
# s = open("../Task files/24.1h.txt").readline().strip()
# s = s.replace('E', 'E E')
# s = s.split()
# print(s)
# mx = 0
# cnt = 0
# # print('y' if "E" in s else 'n')
# for i in s:
#     if ('F' not in i) and (i[0] == 'E' and i[-1] == 'E') and (len(i) >= 12):
#         cnt += 1
# print(cnt)
# answer 9655

# 2
# s = open("../Task files/24.2h.txt").readline().strip()
# s = s.split('E')
# # print(s)
# mx = 0
# for i in s:
#     if i.count('A') >= 3:
#         mx = max(mx, len(i))
# print(mx)
# answer 275

# 3
# s = open("../Task files/24.3h.txt").readline().strip()
# # print(s)
# while 'ad' in s or 'da' in s:
#     if 'ad' in s:
#         s = s.replace('ad', '#')
#     elif 'da' in s:
#         s = s.replace('da', '#')
# s = s.split('#')
# print(s)
# print(len(max(s, key=len)) + 2)
# answer 2250

# 4
# s = open("../Task files/24.4h.txt").readline().strip()
# s = s.replace('AB', '#')
# s = s.replace('AC', '#')
# s = s.replace('AD', '#')
# s = s.replace('OB', '#')
# s = s.replace('OC', '#')
# s = s.replace('OD', '#')
# for i in range(len(s)):
#     if '#'*i in s:
#         print(i)
# answer 202

# 5
# s = open("../Task files/24.5h.txt").readline().strip()
# while 'NPO' in s: s = s.replace('NPO', '#')
# while 'PNO' in s: s = s.replace('PNO', '#')
# # print(s)
# for i in range(len(s)):
#     if '#'*i in s:
#         print(i)
# answer 297

# 6
# s = open("../Task files/24.6h.txt").readlines()
# # print(s[0])
# glob_count_l = 0
# d = {}
# for i in range(len(s)):
#     povtor = 1
#     lenght = ''
#     letter = ''
#     count_l = 0
#     for j in range(len(s[i]) - 1):
#         if s[i][j] == s[i][j+1]:
#             lenght += s[i][j]
#         else:
#             if povtor < len(lenght):
#                 letter = lenght[0]
#             povtor = max(povtor, len(lenght))
#             lenght = ''
#     count_l = s[i].count(letter)
#     d[i] = [letter, povtor, count_l]
# # print(d)
# mx = 0
# st = ''
# key = 0
# for k, v in d.items():
#     if mx < v[1]:
#         mx = v[1]
#         key = k
#         st = v[0]
# print(key, st, mx)
# for k, v in d.items():
#     if v[1] == mx:
#         print(k, v)
# answer 29

# print('| ANSWERS |')
# print('1: 9655')
# print('2: 275')
# print('3: 2252')
# print('4: 202')
# print('5: 297')
# print('6: 29')