1 - Double char
def double_char(str):
  new_string = ''
  for letter in str: 
    new_string += letter*2
  return new_string
2 - Count hi
def count_hi(str):
  return str.count('hi')
3 - Cat_dog
def cat_dog(str):
  return str.count('cat') == str.count('dog')
4 - Count code
def count_code(str):
  count = 0 
  words = ['co'+x+'e' for x in 'abcdefghijklmnopqrstuvwxyz']
  for word in words: 
    numbers = str.count(word)
    count += numbers
  return count
5 - End_other
def end_other(a, b):
  a,b = a.lower(),b.lower() 
  if a.endswith(b) or b.endswith(a):
    return True 
  return False
6 - xyz there
def xyz_there(str):
  a,b = str.count('xyz'),str.count('.xyz')
  if a!=b:
    return True 
  return False