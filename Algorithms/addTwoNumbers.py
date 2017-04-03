# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        re = head
        carry = 0
        while True:
        	# 计算进位
        	if l1 != None:
        		carry += l1.val
        		l1 = l1.next
        	if l2 != None:
        		carry += l2.val
        		l2 = l2.next
        	#现在carry等于两位数相加以及和上次进位数的和
        	re.val = carry % 10
        	carry /= 10

        	if l1 != None or l2 != None or carry != 0:
        		#在re之后加一个值为0的节点
        		re.next = ListNode(0)
        		#将指针指向后一位
        		re = re.next
        	else:
        		break
        return head
