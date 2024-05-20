coordinates = input()
c = coordinates
k = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8}
p,q = int(k[c[0]]),int(c[1])
if p%2 != 0 and q%2 != 0:
    print(False)
if p%2 == 0 and q%2 != 0:
    print(True)
if p%2 != 0 and q%2 == 0:
    print(True)
if p%2 == 0 and q%2 == 0:
    print(False)
        
