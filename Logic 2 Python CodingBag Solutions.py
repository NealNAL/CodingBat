1 - Make bricks
def make_bricks(small, big, goal):
  if (goal//5) <= big: 
       if (goal%5) <= small: 
         return True 
       else: 
         return False
  if (goal//5) >= big:
       if (goal - (big*5)) <= small:
         return True
       else:
         return False
2 - Lone sum
def lone_sum(a, b, c):
  sum = 0
  sum += a if a not in [b,c] else 0
  sum += b if b not in [a,c] else 0
  sum += c if c not in [a,b] else 0
  return sum
3 - Lucky sum
def lucky_sum(a, b, c):
  sum = 0
  list = [a,b,c,13]
  for n in list[:list.index(13)]:
    sum += n
  return sum
4 - No teen sum
def fix_teen(n):
  if n in [13, 14, 17, 18, 19]:
    return 0
  return n
def no_teen_sum(a, b, c):
  return fix_teen(a) + fix_teen(b) + fix_teen(c)
5 - Round sum
def round_sum(a, b, c):
  def round10(num):
    return (num+5)/10*10
  return round10(a)+round10(b)+round10(c)
6 - Close far
def close_far(a, b, c):
  return (abs(abs(b)-abs(c))>=2) and \
  ((abs(abs(b)-abs(a))<=1 and abs(abs(c)-abs(a))>=2) \
  or (abs(abs(c)-abs(a))<=1 and abs(abs(b)-abs(a))>=2))
7 - Make chocolate
def make_chocolate(small, big, goal):
  maxBig = goal / 5
   
  if big >= maxBig:
    if small >= (goal - maxBig * 5):
      return goal - maxBig * 5
  if big < maxBig:
    if small >= (goal - big * 5):
      return goal - big * 5
  return -1