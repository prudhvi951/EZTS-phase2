l = [1,8,9,7,5,3,4]
for i in range(1,len(l)):
    key = l[i]
    j = i - 1
    while j>=0 and l[j]<key:
        l[j+1]=l[j]
        j-=1
    l[j+1] = key
print(l)
        
