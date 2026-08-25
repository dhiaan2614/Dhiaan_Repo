dic1={'Codingal' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}
list1=[]
for i in dic1.values():
    list1.append(i)

value=int(input('Please enter a number'))



frequency=list1.count(value)

print(frequency)