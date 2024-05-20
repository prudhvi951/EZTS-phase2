s = [1,2,3,4,5,6,7,8,9,10,11,12]
n = 3
f = 0
while len(s) >1:
    if f==0:
        for i in range(n):
            if len(s) >1:
                s.pop(0)
            else:
                break
        f = 1
    else:
        for i in range(n):
            if len(s) >1:
                s.pop()
            else:
                break
        f = 0
print(s)
