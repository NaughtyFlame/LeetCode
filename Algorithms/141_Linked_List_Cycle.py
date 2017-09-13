# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return False
        
        p1, p2 = head, head
        
        while True:
            if p1.next != None:
                p1 = p1.next.next
                p2 = p2.next                    
            else:
                return False
            
            if p1 == None or p2 == None:
                return False
            elif p2 == p1.next:
                return True
