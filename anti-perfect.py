#n = int(input('Enter an integer: '))
def anti_perfect(n):
  ls = []
  for i in range(1, n//2+1):
    if n%i == 0:
      ls.append(int(str(i)[::-1]))
  return sum(ls) == n

for i in range(0, 10000):
  if(anti_perfect(i)):
    print(i)
    
print('done')

'''output
0
6
244
285
done
'''

 





   

    


