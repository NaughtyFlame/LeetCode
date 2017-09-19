# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        slow, fast = head, head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        slow = slow.next 
        # 
        slow = self.reverseList(slow)
        
        while slow:
            if head.val != slow.val:
                return False
            slow = slow.next
            head = head.next
        return True
        
    def reverseList(self, head):
        if head == None or head.next == None:
            return head
        p = head.next
        n = self.reverseList(p)
        p.next = head
        head.next = None
        
        return n
