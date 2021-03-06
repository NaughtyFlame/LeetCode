# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head
        while(p != None and p.next != None):
            if p.val != p.next.val:
                p = p.next
            else:
                p.next = p.next.next
        return head
