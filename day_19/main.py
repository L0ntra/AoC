# Given a string and possible replacements...
#
# stirng: HOH
# replacement rules:
# H -> HO
# H -> OH
# O -> HH
#
# How many different strings can be made by replacing exatly 1 character in the
# string using a replacement rule?

class rule:
  def __init__(self, var, val):
    self.var = var
    self.val = val

def read_line(line):
  length = len(line)
  for i in range(length):
    if line[i] == ' ':
      #var, val
      return line[:i], line[i+4:length-1]

def read_file():
  f = open("input.txt")
  line = f.readline()
  rules = []
  while line != '':
    var, val = read_line(line)
    rules += [rule(var, val)]
    line = f.readline()
  return rules

rules = read_file()

s = "CRnSiRnCaPTiMgYCaPTiRnFArSiThFArCaSiThSiThPBCaCaSiRnSiRnTiTiMgArPBCaPMgYPTiRnFArFArCaSiRnBPMgArPRnCaPTiRnFArCaSiThCaCaFArPBCaCaPTiTiRnFArCaSiRnSiAlYSiThRnFArArCaSiRnBFArCaCaSiRnSiThCaCaCaFYCaPTiBCaSiThCaSiThPMgArSiRnCaPBFYCaCaFArCaCaCaCaSiThCaSiRnPRnFArPBSiThPRnFArSiRnMgArCaFYFArCaSiRnSiAlArTiTiTiTiTiTiTiRnPMgArPTiTiTiBSiRnSiAlArTiTiRnPMgArCaFYBPBPTiRnSiRnMgArSiThCaFArCaSiThFArPRnFArCaSiRnTiBSiThSiRnSiAlYCaFArPRnFArSiThCaFArCaCaSiThCaCaCaSiRnPRnCaFArFYPMgArCaPBCaPBSiRnFYPBCaFArCaSiAl"
var = ''
perms = []
for i in range(len(rules)):
  for j in range(len(s)):
    if s[j] >= 'a' and s[j] <= 'z' and s[j] != 'e':
      #lower case. 
      #Add
      var += s[j]
      #Prase
      if var == rules[i].var:
        n_s = s[:j-1] + rules[i].val + s[j+1:]
      else:
        n_s = ''
      #Clear
      var = ''
    else: #or == 'e'
      #Capital
      #parse
      if var == rules[i].var:
        n_s = s[:j-1] + rules[i].val + s[j:]
      else:
        n_s = ''
      #clear / add
      var = s[j]
    if n_s != '':
      perms += [n_s]
      n_s = ''
  if var != '' and var == rules[i].var:
    k = 1
    if len(var) == 1:
      k = 0
    n_s = s[:j-k] + rules[i].val + s[j+1:]
    perms += [n_s]
  var = ''

# Check for dups.
# Scan list looking for dupes.
# Compile a list of indeies
# if list > 1 element:
#   remove all but 1

result = 0
length = len(perms)
i = 0
while i < length:
  if perms.count(perms[i]) > 1:
    perms.remove(perms[i])
    length -= 1
  else:
    result += 1
    i += 1
print(result)

# use while loop. for loops remembers init val






#"CRnSiRnCaPTiMgYCaPTiRnFArSiThFArCaSiThSiThPBCaCaSiRnSiRnTiTiMgArPBCaPMgYPTiRnFArFArCaSiRnBPMgArPRnCaPTiRnFArCaSiThCaCaFArPBCaCaPTiTiRnFArCaSiRnSiAlYSiThRnFArArCaSiRnBFArCaCaSiRnSiThCaCaCaFYCaPTiBCaSiThCaSiThPMgArSiRnCaPBFYCaCaFArCaCaCaCaSiThCaSiRnPRnFArPBSiThPRnFArSiRnMgArCaFYFArCaSiRnSiAlArTiTiTiTiTiTiTiRnPMgArPTiTiTiBSiRnSiAlArTiTiRnPMgArCaFYBPBPTiRnSiRnMgArSiThCaFArCaSiThFArPRnFArCaSiRnTiBSiThSiRnSiAlYCaFArPRnFArSiThCaFArCaCaSiThCaCaCaSiRnPRnCaFArFYPMgArCaPBCaPBSiRnFYPBCaFArCaSiAl"

