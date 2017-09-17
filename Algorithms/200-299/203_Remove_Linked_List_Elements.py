# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head == None:
            return head
        node = head
        head = ListNode(0)
        head.next = node
        pre = head
        while node != None:
            if node.val == val:
                if node.next != None:
                    pre.next = node.next
                    node = pre
                else:
                    pre.next = None
            pre = node
            node = node.next
        return head.next
        
