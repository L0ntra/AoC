f = open("input.txt")
floor = 0
count = 0
result = 0
paren = ' '
while paren != '':
  paren = f.read(1)
  count = count + 1
  if paren == '(':
    floor = floor + 1
  if paren == ')':
    floor = floor - 1
  if result == 0 and floor == -1:
    result = count

print("Final Floor: " + str(floor) + "\nPost of first char to take Santa to floor -1: " + str(result))
