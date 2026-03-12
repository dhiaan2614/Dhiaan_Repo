ms=float(input('Please enter the marks you scored in English'))
ms2=float(input('Please enter the marks you scored in Maths'))
ms3=float(input('Please enter the marks you scored in science'))
ms4=float(input('Please enter the marks you scored in Geography'))
ms5=float(input('Please enter the marks you scored in History'))

avg=(ms+ms2+ms3+ms4+ms5)/5

print(avg)


if avg >90 and avg<100:
    print('Grade A+')
elif avg >80 and avg <90:
    print('Grade A')
elif avg >70 and avg<80:
    print('Grade B')
elif avg >60 and avg <70:
    print('Grade B-')
elif avg >50 and avg<60:
    print("Grade C")
elif avg>40 and avg<50:
    print('Grade C-')
elif avg <40:
    print('FAILED')
