# Write a program to select a ride according to your preference. The ride is divided into two major categories: 1. Bike 2. Car And further, bikes and cars are divided into 2 subcategories. To give the user better selection options.



ques=input('Would you prefer car or bike')



if ques == 'car':
    ques2=input('Would you prefer a Sedan or SUV')
    if ques2.lower() =='sedan':
        print('You have chosen Sedan')
    else:
        print('You have chosen SUV')
else:
    print('You have chosen Bike') 

