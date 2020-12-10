1 - String times
def string_times(str, n):
  return str*n
2 - Front times
def front_times(str, n):
  return str[:3]*n
3 - String bits
def string_bits(str):
  return str[0::2]
4 - String splosion
def string_splosion(str):
  result = ''
  for i in range(len(str)):
    result = result + str[:i+1]
  return result
 5 - Last 2
 def last2(str):
  if len(str) < 2:
    return 0
  last2 = str[len(str)-2:]
  count = 0
  for i in range(len(str)-2):
    sub = str[i:i+2]
    if sub == last2:
      count = count + 1
  return count
 6 - Array count_9
 def array_count9(nums):
  return nums.count(9)
 7 - Array front 9
 def array_front9(nums):
  if len(nums) <= 4: 
    if nums.count(9) >= 1:
      return True 
    else:
      return False 
  else: 
    if nums[:4].count(9) >= 1:
      return True 
    else: 
      return False
8 - Array 123
def array123(nums):
  for i in range(len(nums)-2):
      if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
        return True
  return False
9 - String match
def string_match(a, b):
  shorter = min(len(a), len(b))
  count = 0
  for i in range(shorter-1):
    a_sub = a[i:i+2]
    b_sub = b[i:i+2]
    if a_sub == b_sub:
      count = count + 1
  return count