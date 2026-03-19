medical=input('Do you have a medical need? ')
attendance=int(input('What is your attendance? '))

if medical == 'yes':
    print("You are allowed to sit the exam")
else:
    if attendance >75:
        print('You are allowed to sit in the exam')
    else:
        print('You are not allowed to sit in the exam')