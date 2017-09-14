# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # Calculer the length of two linked list
        len_nodeA, len_nodeB = 1, 1
        nodeA ,nodeB = headA, headB
        if(headA == None or headB == None):
            return None
        while True:
            if nodeA.next == None:
                break
            nodeA = nodeA.next
            len_nodeA += 1
        while True:
            if nodeB.next == None:
                break
            nodeB = nodeB.next
            len_nodeB += 1
            
        if nodeA != nodeB:
            return None
        
        if len_nodeA > len_nodeB:
            for index in range(len_nodeA - len_nodeB):
                headA = headA.next
        else:
            for index in range(len_nodeB - len_nodeA):
                headB = headB.next
        # to find the intersection
        while(headA != headB ):
            headA = headA.next
            headB = headB.next
        
        return headA
        
