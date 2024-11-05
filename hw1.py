khmer = float(input('Your Khmer Score From 0-75: '))
math = float(input('Your Math Score From 0-125:  '))
english = float(input('Your English Score From 0-50: '))
physics = float(input('Your Physics Score From 0-75: '))
chemistry = float(input('Your Chemistry Score From 0-75: '))
total = khmer + math + english + physics + chemistry
if total > 400:
    print('Please input scores again.')
elif 320 <= total <= 40:
    print('You got an A!')
elif 280 <= total < 320:
    print('You got a B!')
elif 240 <= total < 280:
    print('You got a C!')
elif 200 <= total < 240:
    print('You got a D!')
elif 0 <= total < 200:
    print('Sorry, you got an F. Please try again next time.')
else:
    print('Value Error! Input again!')
