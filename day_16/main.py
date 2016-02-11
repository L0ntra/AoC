class aunt:
#  children = cats = samoyeds = pomeranians = akitas = 0
#  vizslas = goldfish = trees = cars = perfumes = 0 
  def __init__(self, name):
    self.name = name
    self.children = self.cats = self.samoyeds = -1
    self.pomeranians = self.akitas = -1
    self.vizslas = self.goldfish = self.trees = -1
    self.cars = self.perfumes = -1

  def add_val(self, item, val):
    setattr(self, item, val)

  def val_match(self, item, val):
    a = getattr(self, item)
    ## Part 2
    if item == 'cats' or item == 'trees':
      if a > val or a == -1:
        return True
      return False
    
    if item == 'pomeranians' or item == 'goldfish':
      if a < val or a == -1:
        return True
      return False
    ## \Part 2
 
    if a == val or a == -1:
      return True
    return False

  def print_all(self):
    print("children:", self.children, "cats:", self.cats, "samoyeds:", self.samoyeds, "pomeranians:", self.pomeranians, "akitas:", self.akitas)
    print("vizslas:", self.vizslas, "goldfish:", self.goldfish, "trees:", self.trees, "cars:", self.cars, "perfumes:", self.perfumes)

def scan_col(line):
  for i in range(len(line)):
    if line[i] == ':':
      return i
      
def scan_com(line):
  for i in range(len(line)):
    if line[i] == ',' or line[i] == '\n':
      return i

def read_line(line, a):
  item = ''
  val = 0
  space = space2 = 0
  space = scan_col(line[space2:]) + space2 + 2
  for i in range(3):
    space2 = space + scan_col(line[space:])
    item = line[space:space2]
    space = scan_com(line[space2+1:]) + space2+1
    val = int(line[space2+1:space])
    space += 2
    a.add_val(item, val)

  return

def elim(aunts, item, val):
  new_aunts = []
  for i in range(len(aunts)):
    if aunts[i].val_match(item, val):
      new_aunts += [aunts[i]]
  return new_aunts


f = open('input.txt')
aunts = []
line = f.readline()
i = 0
while line != '':
  aunts += [aunt(str(i+1))]
  read_line(line, aunts[i])
#  print("Aunt", i)
#  aunts[i].print_all()
  i += 1
  line = f.readline()


print(len(aunts))
aunts = elim(aunts, 'children', 3)
aunts = elim(aunts, 'cats', 7)
aunts = elim(aunts, 'samoyeds', 2)
aunts = elim(aunts, 'pomeranians', 3)
aunts = elim(aunts, 'akitas', 0)
aunts = elim(aunts, 'vizslas', 0)
aunts = elim(aunts, 'goldfish', 5)
aunts = elim(aunts, 'trees', 3)
aunts = elim(aunts, 'cars', 2)
aunts = elim(aunts, 'perfumes', 1)
print(len(aunts))
print(aunts[0].name)
