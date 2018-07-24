def anit_vowel(n):
	v=['a','e','i','o','u']
	char=[]
	for i in n:
		if i not in v:
			char.append(i)
	return "".join(char)
n=list(input("enter the string:"))
print(anit_vowel(n))
