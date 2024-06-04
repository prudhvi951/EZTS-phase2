n = list(map(int, input().split()))
m = int(input())
l = 0
r = len(n) - 1
found = False

while l <= r:
    mid = (l + r) // 2
    if n[mid] == m:
        print("at index ",mid)
        found = True
        break
    elif n[mid] < m:
        l = mid + 1
    else:
        r = mid - 1

if not found:
    print("Element not found in the list")
