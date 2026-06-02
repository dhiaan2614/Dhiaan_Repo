weather =  (1, 0, 0, 0, 1, 1, 0)

weather.count(1)
weather.count(0)

if weather.count(1) >  weather.count(0):
    print('Rainy Season')
else:
    print('Summer Season')