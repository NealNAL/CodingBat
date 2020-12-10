1 - Count evens
def count_evens(nums):
  count = 0 
  for number in nums: 
    if number%2 == 0:
      count += 1
  return count
2 - Big dif
def count_evens(nums):
  count = 0 
  for number in nums: 
    if number%2 == 0:
      count += 1
  return count
3 - Centered average
def centered_average(nums):
  nums.sort()
  return sum(nums[1:-1]) / (len(nums) - 2)
4 - Sum 13
def sum13(nums):
  co=0
  if len(nums)<=0:
    return co
  for a in range(1,len(nums)):
    if nums[a]==13:
      continue
    elif nums[a-1]==13:
      continue
    else:
      co=co+nums[a]      
  if nums[0]!=13:
    co+=nums[0]
  return co
5 - Sum67
def sum67(nums):
  count = 0
  run = False
  
  for n in nums:
    if n == 6:
      run = True
      continue
    if n == 7 and run:
      run = False
      continue
    if not run:  
      count += n
  
  return count
6 - Has22
def has22(nums):
  for i,v in enumerate(nums[:-1]):
    if v == 2 and nums[i+1] == 2:
      return True
  return False