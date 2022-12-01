import __main__
## OPERATIONS ##
#def syn(index, a, b)
# index = current line number
# a = first piece of command (usually the variable)
# b = second piece of command (an amount to jump)
# return index, variable val
# all commands take 3 args and return 2


# r = r/2
def hlf(i, r, b = None):
  return i+1, r/2

# r = r * 3
def tpl(i, r, b = None):
  return i+1, r * 3

# r = r + 1
def inc(i, r, b = None):
  return i+1, r + 1

# jump relitive to current position
def jmp(i, r, n = None): #n = offset
  if n: #if an n i provided we know to do this
    return i + n, r
  else: #if no n then no var infomation was given
    return i + r, 0

# if r is even jump
def jie(i, r, n):
  if r%2 == 0:
    print(r, "is even")
    return jmp(i, r, n)
  return i+1, r

# if r is one jump
def jio(i, r, n):
  if r == 1:
    return jmp(i, r, n)
  return i+1, r
## /OPERATIONS ##



# parse a line in to pieces (command, reg, n
def parse(line):
  length = len(line)
  command = line[:3]
  a = b = None
  for i in range(4, len(line)):
    if line[i] == ' ': #space found
      a = line[4:i-1]
      break
  if not a:
    a = line[4:]
    try:
      a = int(a)
    except:
      None
  else:
    b = line[i+1:]
    try:
      b = int(b)
    except:
      None
  return command, a, b



f = open('input.txt')
l = f.readline().rstrip()
line = []
while l != '':
  line += [parse(l)]
  l = f.readline().rstrip()

length = len(line)
i = j = a = b = temp = val = 0
a = 1 #part 2
while i < length:
  print(i, line[i])
  func = getattr(__main__, line[i][0])
  try:
    var = getattr(__main__, line[i][1])
  except:
    j, val = func(i, line[i][1], line[i][2])
  else:
    j, val = func(i, var, line[i][2])
    setattr(__main__, line[i][1], val)
    print('\t', line[i][1], "=", val)
  i = j

print(a, b)
