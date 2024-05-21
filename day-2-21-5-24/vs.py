class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def insertatbig(self,value):
        newnode = Node(value)
        if self.head==None:
            self.head=newnode
        else:
            newnode.next=self.head
            self.head=newnode
    def insertingatend(self,val):
        newnode=Node(val)
        if self.head==None:
            self.head=newnode
        else:
            curr=self.head
            while curr.next!=None:
                curr=curr.next
            curr.next=newnode
    def printlist(self):
        curr=self.head
        while(curr!=None):
            print(curr.data,end='->')
            curr=curr.next
        print("null")
l=linkedlist()
l.insertatbig(1)
l.insertatbig(2)
l.insertatbig(3)
l.insertatbig(4)
l.insertingatend(6)
l.printlist()
