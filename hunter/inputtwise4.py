
a=int(input('enter an integer'))
n=[int(x) for x in input().split()]
k=0
for i in n:
    k=0
    for j in n:
        if i==j:
            k+=1
    if k==1:
        print(i)
