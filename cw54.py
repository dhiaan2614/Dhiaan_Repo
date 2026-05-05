try:
    num1=int(input('Enter a number: '))
    num2=int(input('Enter a number: '))
    add=num1+num2
    div=num1/num2
    print(add)
    print(div)

except ValueError:
    print('Enter a numerical value')
except ZeroDivisionError:
    print('Division with zero is not allowed')
except NameError:
    print('The name', NameError)

finally:
    print('I will work no matter what happens')