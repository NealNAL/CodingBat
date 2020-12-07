1 - Hello name!
def hello_name(name):
  name = 'Hello',name+'!'
  return ' '.join(name)
2 - Make abba
def make_abba(a, b):
  middle = b*2
  return a+middle+a
3 - Make tags
def make_tags(tag, word):
  tags =  '<'+tag+'>'+word+'</'+tag+'>'
  return tags
4 - Make out word
def make_out_word(out, word):
  return out[:2]+word+out[2:]
5 - Extra end
def extra_end(str):
  return str[-2:]*3
6 - First two
def first_two(str):
  return str[:2]
7 - First half
def first_half(str):
  half = len(str)/2
  return str[:half]
8 - Without end
def without_end(str):
  return str[1:-1]
9 - Combo string
def combo_string(a, b):
  if len(a) > len(b):
    return b+a+b
  else:
    return a+b+a
10 - Non start
def non_start(a, b):
  return a[1:]+b[1:]
11 - Left2
def left2(str):
  return str[2:]+str[:2]