#Leap Year
"""
Year4==0&
Year%100!=0/
Year%400==0

"""


def isLeapYear(Year):
  if (Year % 4 == 0 and Year % 100 !=0) or Year % 400 == 0:
    return True
  else:
    return False


Year = 2012

if isLeapYear(Year):
  print('{} is a leap year.'.format(Year))
else:
  print('{} is not a lepa Year.'.format(Year))
  
  