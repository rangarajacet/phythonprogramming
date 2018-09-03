def reverse(a):
  str = ""
  for i in a:
    str = i + str
  return str
a = input()
r = input() 
t=reverse(a)
u=reverse(r)
print (t+" "+u)
