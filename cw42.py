# 1) Define a function `add(P, Q)` that returns the sum of two numbers (P + Q).
def add(p,q):
    print(p+q)
# 2) Define a function `subtract(P, Q)` that returns the difference of two numbers (P - Q).
def subtract(p,q):
    print(p-q)

# 3) Define a function `multiply(P, Q)` that returns the product of two numbers (P * Q).
def multiply(p,q):
    print(p*q)

# 4) Define a function `divide(P, Q)` that returns the division result of two numbers (P / Q).
def divide(p,q):
    print(p/q)

# 5) Display a menu to the user showing the available operations:
#    a) Add
#    b) Subtract
#    c) Multiply
#    d) Divide
num_1=int(input('Please enter a number: '))
num_2=int(input('Please enter a number: '))

print('Enter 1 to add,Enter 2 to subtract, Enter 3 to multiply, Enter 4 to divide' )

# 6) Take the user's choice as input and store it in `choice`.
choice=int(input())
if choice == 1:
    add(num_1,num_2)
elif choice == 2:
    subtract(num_1,num_2)
elif choice == 3:
    multiply(num_1,num_2)
elif choice == 4:
    divide(num_1,num_2)

# 7) Take two integer inputs from the user:
#    a) Store the first number in `num_1`
#    b) Store the second number in `num_2`


# 8) Use conditional statements to perform the chosen operation:
#    a) If `choice` is 'a', call `add(num_1, num_2)` and print the result.
#    b) Else if `choice` is 'b', call `subtract(num_1, num_2)` and print the result.
#    c) Else if `choice` is 'c', call `multiply(num_1, num_2)` and print the result.
#    d) Else if `choice` is 'd', call `divide(num_1, num_2)` and print the result.

# 9) If the user enters anything other than a/b/c/d, print an invalid input message.


