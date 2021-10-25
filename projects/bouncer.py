# ask for age
age = input('How old are you?\n')

if age != '':
    age = int(age)
    # 18-21 wristband
    if (age >= 18 and age < 21):
        print('You get a wristband for entry')
    # 21+ drink normal entry
    elif age >= 21:
        print('drink like a alcoholic if you want')
    # else too young
    else:
        print('You are too young little one')
else:
    print('Please enter your age!')