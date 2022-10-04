while True:
    name = input("\nEnter the student's name (or 'stop'): ")
    if name == 'stop':
        break
    #For HomeWork
    print('\nHOMEWORKS:')
    HW = []
    for i in range(3):
        while True:
            try:
                hw = eval(input(' Enter HW{x} grade: '.format(x=i)))
                if hw >=0 and hw <= 10:
                    HW.append(hw)
                    break
                else:
                    print(' Grade must be in range [0..10]. Try again.')
                
            except:
                print(' Enter a number.')

    #For Project
    print('\nPROJECTS:')
    PR = []
    for i in range(2):
        while True:
            try:
                pr = eval(input(' Enter Pr{x} grade: '.format(x=i)))
                if pr >=0 and pr <= 100:
                    PR.append(pr)
                    break
                else:
                    print(' Grade must be in range [0..100]. Try again.')
                
            except:
                print(' Enter a number.')
    
    #For EXAMS
    print('\nEXAMS:')
    EX = []
    for i in range(2):
        while True:
            try:
                ex = eval(input(' Enter Ex{x} grade: '.format(x=i)))
                if ex >=0 and ex <= 100:
                    EX.append(ex)
                    break
                else:
                    print(' Grade must be in range [0..100]. Try again.')
                
            except:
                print(' Enter a number.')

    print('\nGrade report for:', name)
    p_HW = (sum(HW)/30)*100
    p_PR = (sum(PR)/200)*100
    p_EX = (sum(EX)/200)*100
    avg = (p_HW + p_PR + p_EX) / 3

    grade = ''
    if avg >= 90:
        grade = 'A'
    elif avg < 90 and avg >= 80:
        grade = 'B'
    elif avg < 80 and avg >= 70:
        grade = 'C'
    elif avg < 70 and avg >= 50:
        grade = 'D'
    elif avg < 60 and avg >= 30:
        grade = 'E'
    else:
        grade = 'F'
                
    print(' Homework average (30% of grade): {:.2f}'.format(p_HW))    
    print(' Project average (30% of grade): {:.2f}'.format(p_PR))
    print(' Other average (40% of grade): {:.2f}'.format(p_EX))
    print(' Student course average: {:.2f}'.format(avg))
    print(' Course grade (CS303E: Fall, 2022):', grade)
    
print('Thanks for using the grade calculator! Goodbye.')
