s = input()
t = input()
d ={}
if len(s) != len(t):
    print(False)
if len(set(s)) != len(set(t)):
    print(False)
for i in range(len(s)):
    if s[i] not in d:
        d[s[i]] = t[i]
    else:
        if t[i] != d[s[i]]:
            print(False)
else:
    print(True)
