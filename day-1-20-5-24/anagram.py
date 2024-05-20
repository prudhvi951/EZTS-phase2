#anagram
s = input()
t = input()
s1 = list(set(s))
t1 = list(set(t))
if len(s1) != len(t1):
    print(False)
if sorted(s1) != sorted(t1):
    print(False)
for i in s1:
    if s.count(i) != t.count(i):
        print(False)
        
else:
    print(True)
