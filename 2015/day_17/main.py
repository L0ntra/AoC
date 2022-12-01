"""count = 0
amount = 150+1
for i in range(amount-1, -1, -20):
  for j in range(0, amount - i, 15):
    for k in range(0, amount - i - j, 10):
      for l in range(amount-1-i-j-k, amount - i - j -k, 5):
        count += 1
print(count)"""

# containers
# 43, 3, 4, 10, 21, 44, 4, 6, 47, 41, 34, 17, 17, 44, 36, 31, 46, 9, 27, 38
c = [43, 3, 4, 10, 21, 44, 4, 6, 47, 41, 34, 17, 17, 44, 36, 31, 46, 9, 27, 38]
a = 0b100000000000000000000
total = 20
count = 0
for i in range(0b11111111111111111111):
  a += 1
#  print(c)
#  print(bin(a)[4:])
  sum_ = 0
  n = 0
  for j in range(20):
    sum_ += int(bin(a)[3+j]) * c[j]
    if int(bin(a)[3+j]) == 1:
      n += 1
  if sum_ == 150:
    if n < total:
      total = n
      count = 0
    if n == total:
      count += 1

print(total)
print(count)
