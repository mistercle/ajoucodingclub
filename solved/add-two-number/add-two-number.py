# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodetoNum(self, node):
        num = 0
        digits = 1
        temp = node
        while True:
            num += temp.val * digits
            if temp.next == None: break
            digits *= 10
            temp = temp.next
        return num
    def numtoNode(self, num):
        node = ListNode()
        r = num % 10
        node.val = r
        q = num // 10
        if q > 0:
            node.next = self.numtoNode(q)
        return node
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = self.nodetoNum(l1)
        n2 = self.nodetoNum(l2)
        return self.numtoNode(n1 + n2)
        