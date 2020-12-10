1 - First last6
def first_last6(nums):
  if nums[0] == 6 or nums[-1] == 6:
    return True 
  else: 
    return False 
2 - Same first last
def same_first_last(nums):
  if len(nums) >= 1 and nums[0]==nums[-1]:
    return True 
  else:
    return False
3 - Make pi
def make_pi():
  return [3,1,4]
4 - Common end
def common_end(a, b):
  if a[0] == b[0] or a[-1] == b[-1]:
    return True 
  else:
    return False
5 - Sum3
def sum3(nums):
  return sum(nums)
6 - Rotate left3
def rotate_left3(nums):
  return [nums[1],nums[2],nums[0]]
7 - Reverse3
def reverse3(nums):
  return nums[::-1]
8 - Max end3
def max_end3(nums):
  return [max(nums[0],nums[-1])]*3
9 - Sum2
def sum2(nums):
  if len(nums) < 2:
    return sum(nums)a
  else:
    return nums[0]+nums[1]
10 - Middle way
def middle_way(a, b):
  len_a,len_b = len(a),len(b)
  return [a[len_a/2],b[len_b/2]]
11 - Make ends
def make_ends(nums):
  return [nums[0],nums[-1]]
12 - Has23
def has23(nums):
  return 2 in nums or 3 in nums