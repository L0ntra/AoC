def on_off(k):
  on = 0
  for i in range(3):
    for j in range(3):
      if k[i][j] == 1 and (j != 1 or i != 1):
        on += 1
  if k[1][1] == 1:
    if on == 2 or on == 3:
      return 1
  elif on == 3:
    return 1
  return 0


def animate(a):
  length = len(a)
  b = [[0 for i in range(length)] for j in range(length)]
  for i in range(length):
    for j in range(length):
      k = [[0,0,0],[0,0,0],[0,0,0]]
      #top left
      if i == 0 and j == 0:
        k[1] = [0] + a[0][0:2]
        k[2] = [0] + a[1][0:2]
      #top right
      elif i ==  0 and j == length-1:
        k[1] = a[0][j-1:length] + [0]
        k[2] = a[1][j-1:length] + [0]
      #bot left
      elif i == length-1 and j == 0:
        k[0] = [0] + a[i-1][0:2]
        k[1] = [0] + a[i][0:2]
      #bot right
      elif i == length -1 and j == length -1:
        k[0] = a[i-1][i-1:length] + [0]
        k[1] = a[i][i-1:length] +[0]
      #top
      elif i == 0:
        k[1] = a[0][j-1:j+2]
        k[2] = a[1][j-1:j+2]
      #bot
      elif i == length-1:
        k[0] = a[i-1][j-1:j+2]
        k[1] = a[i][j-1:j+2]
      #left
      elif j == 0:
        k[0] = [0] + a[i-1][0:2]
        k[1] = [0] + a[i][0:2]
        k[2] = [0] + a[i+1][0:2]
      #right
      elif j == length-1:
        k[0] = a[i-1][j-1:length] + [0]
        k[1] = a[i][j-1:length] + [0]
        k[2] = a[i+1][j-1:length] + [0]        
      else:
        k[0] = a[i-1][j-1:j+2]
        k[1] = a[i][j-1:j+2]
        k[2] = a[i+1][j-1:j+2]
      b[i][j] = on_off(k)
      #part 2
      if ((i == 0 and j == 0) or (i == 0 and j == length-1) or
          (i == length-1 and j == 0) or (i == length -1 and j == length -1)):
          b[i][j] = 1
      #\part2
  return b

def read_file():
  f = open('input.txt')
  a = []
  for j in range(100):
    a += [[int(f.read(1)) for i in range(100)]]
    f.read(1)
  return a

a = read_file()
for j in range(100):
  a = animate(a)

count = 0
for i in range(len(a)):
  for j in range(len(a[0])):
    count += a[i][j]
print(count)






