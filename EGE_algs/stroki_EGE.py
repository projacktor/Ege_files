'''a = [0]
for i in range(200, 1_000):
    s = i * '1'
    while '1111' in s:
        s = s.replace('1111', '22', 1)
        s = s.replace('222', '1', 1)
    print(s, s.count('1'), i)
    print(a)
    a.append(s.count('1'))
    if s.count('1') < min(a[1:]):
        print(s.count('1'), s, i, 'siuuu')

# 200
'''

'''
s = 96 * '9'
while '22222' in s or '9999' in s:
    if '22222' in s:
        s = s.replace('22222', '99', 1)
    else:
        s = s.replace('9999', '2', 1)
print(s)

# 299
'''

'''for i in range(1, 100):
    for j in range(1, 100):
        for k in range(1, 100):
            s = '0' + '1' * i + '2' * j + '3' * k + '0'
            while '00' not in s:
                s = s.replace('01', '210', 1)
                s = s.replace('02', '3101', 1)
                s = s.replace('03', '2012', 1)
            if s.count('1') == 61 and s.count('2') == 50 and s.count('3') == 18:
                print(i, j, k)
                s = '0' + '1' * i + '2' * j + '3' * k + '0'
                print(s)
                break
# 38
'''


from math import sqrt


def delt(n):
    cnt = 0
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            cnt += 1
    if cnt >= 3:
        return True
    else:
        return False


for m in range(1, 100):
    s = '>' + 17 * '1' + 34 * '2' + m * '3'
    while '>1' in s or '>2' in s or '>3' in s:
        if '>1' in s:
            s = s.replace('>1', '22>', 1)
        elif '>2' in s:
            s = s.replace('>2', '2>', 1)
        elif '>3' in s:
            s = s.replace('>3', '1>', 1)
    print(s[:-1])
    if delt(int(s[:-1])):
        print(m)


#
# class Solution:
#     def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
#         a = numBottles
#         b = numExchange
#         cnt = a
#         while a >= b:
#             print(a)
#             cnt += a // b
#             a = a // b + a % b
#         return cnt
#
# print(Solution().numWaterBottles(15, 4))