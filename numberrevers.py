def reverse(n):
  str = ""
  for s in n:
    str = s + str
  return str
n = raw_input()
print (reverse(n))
