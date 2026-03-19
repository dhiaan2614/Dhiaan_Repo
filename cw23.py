# Write a program to calculate the electricity bill. The bill is calculated by checking the number of units consumed. Suppose the user is consuming less than 50 units. The per-unit cost will be 2.60, and the tax on that bill will be 25. If a user is consuming more than 50 but less than 100. Then the per-unit cost will be 3.25, and the tax on that bill will be 35 If the user is coming more than 100 and less than 200. Then the per-unit cost will be 5.26, and the tax will be 45 And above 200, the cost of the unit is 8.45, and the tax is 75.

units=int(input('How many units are you consuming? '))


if units <50:
    amt=(2.60*units)+25
    print(amt)
elif units >50 and units <100:
    amt1=(3.25*units)+35
    print(amt1)
elif units >100 and units <200:
    amt2=(5.26*units)+45
    print(amt2)
elif units>200:
    amt3=(8.45*units)+75
    print(amt3)