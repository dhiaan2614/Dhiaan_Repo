h=float(input('What is you height in meters?'))
w=float(input('What is your weight in kilograms?'))

bmi=w/(h**2)

print('The bmi is',bmi)



if bmi <18.5:
    print('You are underweight')
elif bmi>18.5 and bmi <24.9:
    print('You are normal')
elif bmi>25 and bmi<29.9:
    print('You are overweight')
elif bmi >30 and bmi<34.9:
    print('You have obesity class 1')
elif bmi >35 and bmi<39.9:
    print('You are in obesity class 2')
elif bmi>40:
    print('You have severe obesity')








# Below 18.5 → Underweight

# 18.5 – 24.9 → Healthy / Normal weight

# 25.0 – 29.9 → Overweight

# 30.0 – 34.9 → Obesity (Class I)

# 35.0 – 39.9 → Obesity (Class II)

# 40 and above → Severe / Class III obesity