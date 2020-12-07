1 - Cigar party
def cigar_party(cigars, is_weekend):
  if is_weekend:
    return  cigars >= 40
  else: 
    return 40<=cigars<=60
2 - Date party
def date_fashion(you, date):
  if you <= 2 or date <=2:
    return 0
  elif you >=8 or date >=8:
    return 2
  else:
    return 1
3 - Squirrel play
def squirrel_play(temp, is_summer):
  if is_summer: 
    if temp >= 60 and temp <= 100:
      return True
    else:
      return False
  else:
    if temp >= 60 and temp <= 90:
      return True 
    else:
      return False
4 - Caught speeding
def caught_speeding(speed, is_birthday):
  if is_birthday: 
    if speed <= 65: 
      return 0 
    elif speed > 65 and speed <= 85:
      return 1 
    else: 
      return 2
  else:
    if speed <= 60:
      return 0 
    elif speed > 60 and speed <= 80:
      return 1 
    else:
      return 2
5 - Sorta sum
def sorta_sum(a, b):
  if a+b >= 10 and a+b<= 19:
    return 20
  else:
    return a+b
6 - Alarm clock
def alarm_clock(day, vacation):
  #Weekdays = 1 - 5 , Weekends = 6 and 0 
  if not vacation: 
    if day >= 1 and day <= 5: 
      return '7:00'
    else:
      return '10:00'
  else: 
    if day >= 1 and day <= 5: 
      return '10:00'
    else:
      return 'off'
7 - Love6
def love6(a, b):
  if (a==6 or b==6) or (a+b == 6) or (abs(a-b) == 6):
    return True 
  else:
    return False
8 - in1to10
def in1to10(n, outside_mode):
  if outside_mode: 
    if n <= 1 or n >= 10:
      return True 
    return False 
  else: 
    if n >= 1 and n <= 10:
      return True 
    return False
9 - Near10
def near_ten(num):
  return (num + 2) % 10 <= 4