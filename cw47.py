# Recursive Function/Recursion

def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
    
n1=int(input('Please enter a number: '))
print(fact(n1))