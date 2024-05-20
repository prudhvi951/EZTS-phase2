n = input()
k = []
for i in n:
    if i.isdigit():
        k.append(int(i))
    else:
        if i == "+":
            c = k[-1]+k[-2]
            k.pop()
            k.pop()
            k.append(c)
        if i == "-":
            c = k[-1] - k[-2]
            k.pop()
            k.pop()
            k.append(c)
        if i == "*":
            c = k[-1]*k[-2]
            k.pop()
            k.pop()
            k.append(c)
        if i == "/":
            c = k[-1]//k[-2]
            k.pop()
            k.pop()
            k.append(c)
print(*k)
