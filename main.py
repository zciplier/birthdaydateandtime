import datetime
x = datetime.datetime.now()
birthyear = input("What is your birth date? ")
age = x.year - int(birthyear)
if age > 0:
  if age == 1:
    print('You are', age, 'year old.')
  else:
    print('You are', age, 'years old.')
elif age == 0:
   print('You were just born this year at', age, 'years old!')
else:
   print('Try again, \'Time Traveler\'.')
