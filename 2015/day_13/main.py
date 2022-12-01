class vert:
  def __init__(self, name):
    self.name = name
    self.edges = []
    self.visited = False
    return

  def highest_cost(self, start_edge = None): 
    #c_cost = current_cost
    if len(self.edges) == 0:
      return 0

    self.visited = True
    temp_cost = 0
    prev_cost = -1000
    for i in range(0, len(self.edges)):
      if not self.edges[i].tar.visited:
        temp_cost = self.edges[i].tar.highest_cost(start_edge) + self.edges[i].cost
        if temp_cost > prev_cost:
          prev_cost = temp_cost
    self.visited = False
    if prev_cost == -1000:
      prev_cost = self.find_edge(start_edge.name).cost
    return prev_cost

  def add_edge(self, e):
    found = False
    for i in range(len(self.edges)):
      if self.edges[i].tar.name == e.tar.name:
        self.edges[i].cost += e.cost
        found = True
        break
    if not found:
      self.edges += [e]
    found = False

    for i in range(len(e.tar.edges)):
      if self.name == e.tar.edges[i].tar.name:
        e.tar.edges[i].cost += e.cost
        found = True
        break
    if not found:
      e.tar.edges += [edge(self, e.cost)]
    return 

  def find_vert(self, vert_name):
    found = None
    if self.name == vert_name:
      return self
    self.visited = True
    for i in range(len(self.edges)):
      if not self.edges[i].tar.visited:
        found = self.edges[i].tar.find_vert(vert_name)
        if found:
          return found
    self.visited = False
    return None

  def find_edge(self, tar_name):
    if not len(self.edges):
      return None #No edges yet
    length = len(self.edges)
    for i in range(length):
      if self.edges[i].tar.name == tar_name:
        return self.edges[i] #found
    return None #not found

  def print_all(self):
    self.visited = True
    print(self.name, 'to:', end = '\t')
    for i in range(len(self.edges)):
      print(self.edges[i].tar.name, self.edges[i].cost, end = ', ')
    print()
    for i in range(len(self.edges)):
      if not self.edges[i].tar.visited:
        self.edges[i].tar.print_all()
        self.visited = False
        return
    self.visited = False
    return

class edge:
  def __init__(self, tar, cost):
    self.tar = tar
    self. cost = cost



def part_line(line):
  space = val = 0
  source = target = ''
  length = len(line)

  for i in range(length):
    if line[i] == ' ':
      source = line[:i]
      space = i+1
      break
  for i in range(space, length):
    if line[i] == ' ':
      val = int(line[space:i])
      target = line[i+1:length-1]
      break
  return source, target, val



f = open('input.txt')
line = f.readline()
verts = []

while line != '':
  s, t, v = part_line(line)
  x = y = -1  
  for i in range(len(verts)):
    if verts[i].name == s:
      x = i
      break
  for j in range(len(verts)):
    if verts[j].name == t:
      y = j
      break
  line = ''

  if x < 0:
    verts += [vert(s)]
    x = len(verts)-1
  if y < 0:
    verts += [vert(t)]
    y = len(verts)-1

  verts[x].add_edge(edge(verts[y], v))
  line = f.readline()
#part 2
length = len(verts)
my_vert = vert('me')
for i in range(length):
  verts[i].add_edge(edge(my_vert, 0))
verts += [my_vert]
#/part2

for i in range(len(verts)):
  print(verts[i].highest_cost(verts[i]))
