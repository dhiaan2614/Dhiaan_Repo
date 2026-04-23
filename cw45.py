# Finding Cube


def cube(num1):
    print('The cube of', num1, 'is', num1**3 )

def div3():
    x=int(input('Please enter the number you want to find the cube of: '))
    if x%3==0:
        cube(x)
    else:
        print('Since the number is not divisible by 3 we are not printing it')
div3()
   
