# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a = headA
        b = headB
        while a!=b:
            c = 0
            if a == None:
                a = headB
            else:
                a = a.next
            if b == None:
                b = headA
                c =c +1
            else:
                b = b.next
            if c>2:
                return null
        return a
