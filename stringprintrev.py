def reverse(s):
  str = ""
  for r in s:
    str = r + str
  return str
s = raw_input()
print (reverse(s))
