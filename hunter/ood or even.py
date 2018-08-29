def odd even():
	n=int(input())
	l=[]
	for i in range(n):
		l.append(int(input()))
	o,e=[],[]
	for i in range(n):
		if i%3==0 and l[i]%3!=0:
			o.append(l[i])
		elif i%3!=0 and l[i]%3==0:
			o.append(l[i])
	print(o)
try:
	odd even()
except:
	print('invalid')
