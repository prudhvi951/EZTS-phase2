class node:
    def __init__(self,data):
        self.data = data
        self.next = None
a = node(1)
b = node(2)
c = node(3)
a.next = b
b.next = c
print(a)
print(b)
print(a.data)
print(a.next)
print(a.next.next.data)
