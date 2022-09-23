'''
Number equal to the sum of powers of its digits
Finding all 7 digits number

Between 1000000 and 9999999
'''
print('start')
k = 0
for i in range(1000000, 10000000):
    k += 1
    if k%999999 == 0:
        print('Number checked = ',k)
    n = i
    s = 0
    while i:
        r = i % 10
        r = r ** 7
        s = s + r
        i = i // 10
    if s == n:
        print('================> Number found = ',s)
print('end')
