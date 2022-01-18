# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self, l1, l2):
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.merge(l1.next, l2)

        return l1 or l2

    def sortList(self, head: ListNode) -> ListNode:
        if not (head and head.next): 
            return head

        mid, slow, fast = None, head, head

        while fast and fast.next:
            mid, slow, fast = slow, slow.next, fast.next.next

        mid.next = None

        l1 = self.sortList(head) 
        l2 = self.sortList(slow)

        return self.merge(l1, l2)
        