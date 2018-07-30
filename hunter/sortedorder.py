a=1234567
check= 1234665758
n=str(a)
m=str(check)
for i in n:
  count = m.count(i)
  if (count>1):
   print (i,count)
