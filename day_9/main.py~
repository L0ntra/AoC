class vert():
  def __init__(self, name):
    self.name = name
    self.edges = []
    self.visited = False

  def add_edge(self, e):
    self.edges = self.edges + [e]
    return

  def print_all(self):
    self.visited = True
    print(self.name)
    for i in range(len(self.edges)):
      if not self.edges[i].tar.visited:
        self.edges[i].tar.print_all()
        break
    self.visited = False
    return

  def shortest_dist(self, total):
    self.visited = True
    temp_dist = 0
    prev_dist = -0
    for i in range(len(self.edges)):
      if not self.edges[i].tar.visited:
        #is the path shorter than the others traveled?
        temp_dist = self.edges[i].tar.shortest_dist(self.edges[i].dist)
        if temp_dist < prev_dist or prev_dist == -0:
          prev_dist = temp_dist
    self.visited = False
    return total + prev_dist
 
  def longest_dist(self, total):
    self.visited = True
    temp_dist = 0
    prev_dist = -0
    for i in range(len(self.edges)):
      if not self.edges[i].tar.visited:
        #is the path shorter than the others traveled?
        temp_dist = self.edges[i].tar.longest_dist(self.edges[i].dist)
        if temp_dist > prev_dist or prev_dist == -0:
          prev_dist = temp_dist
    self.visited = False
    return total + prev_dist    

  def find_vert(self, name):
    found = None
    if self.name == name:
      return self
    self.visited = True
    for i in range(len(self.edges)):
      if not self.edges[i].tar.visited:
        found = self.edges[i].tar.find_vert(name)
        if found:
          break
    self.visited = False
    return found


class edge:
  def __init__(self, target, distance):
    self.tar = target
    self.dist = distance

  def ret():
    return self.tar, self.dist




def break_line(line): #start to end = dist
  length = len(line)
  space = dist = 0
  start = end = ''
  for i in range(length):
    if line[i] == ' ':
      start = line[0:i]
      space = i +4  # +3 skips 'to '
      break
  for i in range(space, length):
    if line[i] == ' ':
      end = line[space:i]
      dist = int(line[i+2:length-1]) # +3 skips '= ', len -1 removes the /n
      break
  return (start, end , dist)

def read_file():
  s_vert = e_vert = None
  dist = 0
  verts = []
  f = open('input.txt')
  line = f.readline()
  while line != '':
    start, end, dist = break_line(line)
#    print(start, '|' , end, '|' , dist)
    if not len(verts): #EMPTY LIST:
      s_vert = None
      e_vert = None
    else:
      s_vert = verts[0].find_vert(start)
      e_vert = verts[0].find_vert(end)
    if not s_vert:
      s_vert = vert(start)
      verts += [s_vert]
    if not e_vert:
      e_vert = vert(end)
      verts += [e_vert]

    s_vert.add_edge(edge(e_vert, dist))
    e_vert.add_edge(edge(s_vert, dist))

    #ALG. for adding a conncetion
    # 1 Search Verts for start and end
    # 1.1 if start or end are not in graph add them to a list of verts 
    # 2. create edge from start to end and add to starts edges
    # 3. create edge from end to start and add to ends edges
    # 4. return the list of verts
    #END ALG

    line = f.readline()
  return verts

verts = read_file()
j = k = 0
for i in range(len(verts)):
  j = verts[i].shortest_dist(0)
  if j < k or k == 0:
    k = j
print("Shortest distance:", k)

j = k = 0
for i in range(len(verts)):
  j = verts[i].longest_dist(0)
  if j > k:
    k = j
print("Longest distance:", k)

"""
a = vert('a')
b = vert('b')
c = vert('c')
d = vert('d')

a.add_edge(edge(b, 3))
a.add_edge(edge(c, 4))
a.add_edge(edge(d, 5))

b.add_edge(edge(a, 6))
b.add_edge(edge(c, 7))
b.add_edge(edge(d, 8))

c.add_edge(edge(a, 9))
c.add_edge(edge(b, 10))
c.add_edge(edge(d, 11))

d.add_edge(edge(a, 12))
d.add_edge(edge(b, 13))
d.add_edge(edge(c, 14))

a.print_all()
print('----')
b.print_all()
print('----')
c.print_all()
print('----')
d.print_all()
print('----')

print(a.shortest_dist(0))
print(b.shortest_dist(0))
print(c.shortest_dist(0))
print(d.shortest_dist(0))

print(a.find_vert('a').name)
print(a.find_vert('b').name)
print(a.find_vert('c').name)
print(a.find_vert('d').name)

print(b.find_vert('a').name)
print(b.find_vert('b').name)
print(b.find_vert('c').name)
print(b.find_vert('d').name)

print(c.find_vert('a').name)
print(c.find_vert('b').name)
print(c.find_vert('c').name)
print(c.find_vert('d').name)

print(d.find_vert('a').name)
print(d.find_vert('b').name)
print(d.find_vert('c').name)
print(d.find_vert('d').name)
"""
