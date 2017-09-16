# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        res = []
        tr = root
        if tr == None:
            return []
        while tr != None or len(stack) > 0:
            while tr != None:
                res.append(tr.val)
                stack.append(tr)
                tr = tr.left
            tr = stack.pop()
            tr = tr.right
        return res
