f = open('input.txt')

x = y = 0
up = down = left = right = 0

direction = ' '
while direction != '':
  direction = f.read(1)
  if direction == '^':
    y += 1
  if direction == 'v':
    y -= 1
  if direction == '>':
    x += 1
  if direction == '<':    
    x -= 1

  if x > right:
    right = x
  if x < left:
    left = x
  if y > up:
    up = y
  if y < down:
    down = y

print("up ", up)
print("down ", down)
print("left ", left)
print("right ", right)
print("Max Heigth ", up - down)
print("Max Width ", right - left)

grid = [[0 for j in range(2*(right - left + 2))] for i in range(2*(up - down + 2))]
print(len(grid) * len(grid[0]))

x = -1 * left
y = -1 * down
x2 = x
y2 = y

f.seek(0,0)
direction = ' '
grid[y][x] = 1
diff_houses = 1





while direction != '':
  direction = f.read(1)
  if direction == '^':
    y += 1
  if direction == 'v':
    y -= 1
  if direction == '>':
    x += 1
  if direction == '<':
    x -= 1
  if grid[y][x] == 0:
    diff_houses += 1
  grid[y][x] += 1

  direction = f.read(1)
  if direction == '^':
    y2 += 1
  if direction == 'v':
    y2 -= 1
  if direction == '>':
    x2 += 1
  if direction == '<':
    x2 -= 1
  if grid[y2][x2] == 0:
    diff_houses += 1
  grid[y2][x2] += 1


print("Different houses visited: " + str(diff_houses))






