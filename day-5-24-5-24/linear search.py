n = list(map(int,input().split()))
m = int(input())
le = len(n)
res = -1
i = 0
while i < le:
    if n[i] == m:
        res = i 
        break  
    i += 1  
if res != -1:
    print(f"Element found at index {res}")
else:
    print("Element not found in the list")
