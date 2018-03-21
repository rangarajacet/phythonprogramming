def Power(a,y):
    if (a == 0):
        return False
    while (a != 1):
            if (a % y != 0):
                return False
            a = a // y
             
    return True
b=int(input())
c=int(input())
if(Power(b,c)):
    print('Yes')
else:
    print('No')
