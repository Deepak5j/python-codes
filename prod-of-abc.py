'''
a, b, c belongs N
a + b + c = 100
1/a + 1/b + 1/c = 1/9
abc = ?


Code generate ans as :-
a= 16 	b= 36 	c= 48
abc= 27648

Only 16, 36 and 48 are unique values

'''
for a in range(1, 101):
    for b in range(1, 101):
        for c in range(1, 101):
            if a+b+c == 100:
                if 1/a + 1/b + 1/c == 1/9:
                    print('a=',a, '\tb=',b, '\tc=',c)
                    print('abc=', a*b*c)
                    print()
