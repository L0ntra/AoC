
def read_input(dim):
  length = len(dim)
  start = 0
  for i in range(length):
    if dim[i] == 'x':
      x = int(dim[start:i])
      start = i +1
      break

  for i in range(start, length):    
    if dim[i] == 'x':
      y = int(dim[start:i])
      start = i +1
      break    
  z = int(dim[start:])
  return (x, y, z)




def main():
  f = open("input.txt")
  total_paper = 0
  total_ribbon = 0
  line = f.readline()
  while line != '':
    small = 0
    x, y, z = read_input(line)

    ## Wrapping Paper
    s1 = x * y
    s2 = x * z
    s3 = y * z
    small = s1
    if s2 < small:
      small = s2
    if s3 < small:
      small = s3

    ## Ribbon
    ribbon = 0
    if x <= z and y <= z:
      ribbon = 2*x + 2*y
    if x <= y and z <= y:
      ribbon = 2*x + 2*z
    if y <= x and z <= x:
      ribbon = 2*y + 2*z
    assert ribbon != 0
    total_ribbon = total_ribbon + ribbon + x * y * z
    total_paper = total_paper + 2*s1 + 2*s2 + 2*s3 + small
    line = f.readline()
  print("Paper needed: " + str(total_paper))
  print("Ribbon needed: " + str(total_ribbon))




if __name__ == "__main__":
  main()
