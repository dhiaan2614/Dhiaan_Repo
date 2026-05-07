import random
number=(random.randint(1,3))

if number==1:
    Computer='Rock'
elif number==2:
    Computer='Paper'
else:
    Computer='Scissors'

user=input('Please enter rock, paper or scissors')

if user=='rock'or 'Rock':
    if Computer=='Rock':
        print('It is a tie!')
    elif Computer=='Paper':
        print('Computer Wins!!')
    elif Computer=='Scissors':
        print('User Wins!!')
elif user=='paper'or 'Paper':
    if Computer=='Rock':
        print('User Wins!')
    elif Computer=='Paper':
        print('It is a tie!')
    elif Computer=='Scissors':
        print('Computer Wins!!')
elif user=='scissors'or 'Scissors':
    if Computer=='Rock':
        print('Computer Wins!')
    elif Computer=='Paper':
        print('User Wins!!')
    elif Computer=='Scissors':
        print(' It is a tie!!')
    
print(Computer)
