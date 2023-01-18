r = 1

while r == 1:
    year = int(input('Enter a year: '))
    if year < 1582:
        print('Not within the Greogrian Calendar period')
        year = int(input('Enter a year: '))
    if year % 4 > 0:
        print('Common year')
    elif year % 100 > 0:
        print('Leap year')
    elif year % 400 > 0:
        print('Common year')
    else:
        print('Leap year')
    r = int(input('Do you wanna check more years? 1 - Yes, 0 - No: '))



