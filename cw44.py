bill=int(input('Please enter the bill amount: '))

def total_calc():
    tip=int(input("Please enter the percentage you would like to tip: "))
    total= (bill/tip)+bill
    print(total)
total_calc()