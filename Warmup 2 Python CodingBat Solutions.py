1 - String times

#Given a string and a non-negative int n, return a larger string that is n copies of the original string.

#string_times('Hi', 2) → 'HiHi'
#string_times('Hi', 3) → 'HiHiHi'
#string_times('Hi', 1) → 'Hi'

def string_times(str, n):
  return str*n

2 - Front times

#Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front;

#front_times('Chocolate', 2) → 'ChoCho'
#front_times('Chocolate', 3) → 'ChoChoCho'
#front_times('Abc', 3) → 'AbcAbcAbc'

def front_times(str, n):
  return str[:3]*n

3 - String bits

#Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".

#string_bits('Hello') → 'Hlo'
#string_bits('Hi') → 'H'
#string_bits('Heeololeo') → 'Hello'

def string_bits(str):
  return str[0::2]

4 - String splosion

#Given a non-empty string like "Code" return a string like "CCoCodCode".

#string_splosion('Code') → 'CCoCodCode'
#string_splosion('abc') → 'aababc'
#string_splosion('ab') → 'aab'

def string_splosion(str):
  result = ''
  for i in range(len(str)):
    result = result + str[:i+1]
  return result
 
5 - Last 2
 
#Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).

#last2('hixxhi') → 1
#last2('xaxxaxaxx') → 1
#last2('axxxaaxx') → 2
 
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
 
#Given an array of ints, return the number of 9's in the array.

#array_count9([1, 2, 9]) → 1
#array_count9([1, 9, 9]) → 2
#array_count9([1, 9, 9, 3, 9]) → 3
 
 def array_count9(nums):
  return nums.count(9)

7 - Array front 9

#Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.

#array_front9([1, 2, 9, 3, 4]) → True
#array_front9([1, 2, 3, 4, 9]) → False
#array_front9([1, 2, 3, 4, 5]) → False

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

#Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.

#array123([1, 1, 2, 3, 1]) → True
#array123([1, 1, 2, 4, 1]) → False
#array123([1, 1, 2, 1, 2, 3]) → True

def array123(nums):
  for i in range(len(nums)-2):
      if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
        return True
  return False

9 - String match

#Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.

#string_match('xxcaazz', 'xxbaaz') → 3
#string_match('abc', 'abc') → 2
#string_match('abc', 'axc') → 0

def string_match(a, b):
  shorter = min(len(a), len(b))
  count = 0
  for i in range(shorter-1):
    a_sub = a[i:i+2]
    b_sub = b[i:i+2]
    if a_sub == b_sub:
      count = count + 1
  return count