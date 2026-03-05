cost=int(input('Please state the cost of the orange you bought:'))
sell = int(input('Please state the cost of the orange you sold'))

profit= sell-cost
if profit >0:
    print('You are in a profit')
elif profit ==0:
    print('No Profit, No Loss')
else:print('You are in a loss')



