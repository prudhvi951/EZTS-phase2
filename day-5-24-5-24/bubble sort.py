l = [1,2,6,4,3,5]
for i in range(len(l)):
    for j in range(len(l)-1-i):
        if l[j]>l[j+1]:
            l[j],l[j+1] = l[j+1],l[j]
print(l)
