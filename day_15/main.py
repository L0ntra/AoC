class item:
  def __init__(self, name, cap, dur, flav, text, cal):
    self.name = name
    self.cap = cap
    self.dur = dur
    self.fla = flav
    self.tex = text
    self.cal = cal
    return


it = [item('Frosting', 4, -2, 0, 0, 5),
      item('Candy', 0, 5, -1, 0, 8),
      item('Butterscotch', -1, 0, 5, 0, 6),
      item('Sugar', 0, 0, -2, 2, 1)]
cap = dur = flav = text = total = 0
for i in range(100, -1, -1):
  for j in range(0, 101 - i):
    for k in range(0, 101-i-j):
      for l in range(100-i-j-k, 101-i-j-k):
        cap = it[0].cap * i + it[1].cap * j + it[2].cap * k + it[3].cap * l
        dur = it[0].dur * i + it[1].dur * j + it[2].dur * k + it[3].dur * l
        fla = it[0].fla * i + it[1].fla * j + it[2].fla * k + it[3].fla * l
        tex = it[0].tex * i + it[1].tex * j + it[2].tex * k + it[3].tex * l
        cal = it[0].cal * i + it[1].cal * j + it[2].cal * k + it[3].cal * l
        if cap < 0 or dur < 0 or fla < 0 or tex < 0:
          cap = dur = fla = tex = 0
        temp = cap * dur * fla * tex
        if temp > total and cal == 500:
          print(i, j, k, l, '=', i+j+k+l)
          print(cap, dur, fla, tex)
          total = temp
          print(total)

#        print(i, j, k, l, sep = ' | ')
#        input()
print(total)


