class node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkList:
    def __init__(self):
        self.head = None
        self.count = 0
    def insatbeg(self,value):
        newnode = node(value)
        if self.head == None:
            self.head = newnode
        else:
            newnode.next = self.head
            self.head = newnode
    def delatbeg(self):
        if self.head == None:
            print("Empty list")
            return 0
        else:
            self.head = self.head.next
    def delatend(self):
        if self.head == None:
            print("Empty list")
            return 0
        else:
            curr = self.head
            while curr.next.next != None:
                curr = curr.next
            curr.next = None
    def insatend(self,value):
        newnode = node(value)
        if self.head == None:
            self.head = newnode
        else:
            curr = self.head
            while curr.next!= None:
                curr = curr.next
            curr.next= newnode
    def printlist(self):
        curr = self.head
        while curr != None:
            print(curr.data,end="->")
            curr = curr.next
        print("null")
    def countlist(self):
        if self.head == None:
            self.count = 0
        else:
            self.count = 0
            curr = self.head
            while curr != None:
                self.count = self.count+1
                curr = curr.next
            print(self.count)
    
    def addatmid(self,value):
        newnode = node(value)
        if self.head == None:
            self.head = newnode
        if self.head.next == None:
            self.head.next = newnode
        else:
            t = self.head
            r = self.head
            while r.next != None and r.next.next != None:
                t = t.next
                r = r.next.next
            newnode.next = t.next
            t.next = newnode
            
    def delatmid(self):
        if self.head == None:
            print("empty")
        if self.head.next == None:
            print("empty")
        else:
            t = self.head
            r = self.head
            temp = None
            while r.next!= None and r.next.next != None:
                temp = t
                t = t.next
                r = r.next.next
            temp.next = t.next
    def reverse(self):
        prev = None
        nex = None
        cur = self.head
        while cur != None:
            nex = cur.next
            cur.next = prev
            prev = cur
            cur = nex
        self.head = prev
        

k = LinkList()
k.insatbeg(1)
k.insatbeg(2)
k.insatbeg(4)
k.insatbeg(5)
k.addatmid(3)
k.delatmid()
k.reverse()
k.printlist()

k.reverse()
k.printlist()
