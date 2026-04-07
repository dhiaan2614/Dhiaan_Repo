character=input('Please enter a character: ')
count=0
word='god'
for i in word:
    if i == character:
        count+=1
if count>0:
    print('You have 1 or more similar characters')
else:
    print('You have no similar characters')


