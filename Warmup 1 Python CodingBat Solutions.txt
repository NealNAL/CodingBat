1 - Sleep in
def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True 
  else:
    return False
2 - Monkey trouble
def monkey_trouble(a_smile, b_smile):
  if (a_smile and b_smile) or (not a_smile and not b_smile):
    return True 
  else:
    return False
3 - Sum double
def sum_double(a, b):
  if a == b:
    return (a+b)*2
  else:
    return a+b
4 - diff21
def diff21(n):
  if n <= 21: 
    return abs(n-21)
  else:
    return abs(n-21)*2
5 - Parrot trouble
def parrot_trouble(talking, hour):
  if talking and (hour > 20 or hour < 7):
    return True 
  else:
    return False
6 - Makes 10
def makes10(a, b):
  if (a == 10 or b == 10) or a+b == 10:
    return True 
  else:
    return False
7 - Near hundred
def near_hundred(n):
  if (abs(100-n) <= 10) or (abs(200-n) <=10):
    return True 
  else:
    return False
8 - PosNeg
def pos_neg(a, b, negative):
  if ((a < 0 and b >= 0) or (b < 0 and a >= 0 )) and not negative:
    return True 
  elif negative: 
    if a < 0 and b < 0:
      return True 
    else:
      return False
  else:
    return False
9 - Not string
def not_string(string):
  if string.startswith('not'):
    return string
  else:
    string = 'not',string
    return ' '.join(string)
10 - Missing char
def missing_char(string, n):
  string = list(string)
  string[n] = ''
  return ''.join(string)
11 - Front back
def front_back(str):
  if len(str) <= 1:
    return str
  mid = str[1:len(str)-1]  # can be written as str[1:-1]
  return str[len(str)-1] + mid + str[0]
 12 - Front 3
 def front3(str):
  return str[:3]*3