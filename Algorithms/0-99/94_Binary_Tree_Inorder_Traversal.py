# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        res = []
        tr = root
        while tr or stack:
            if tr:
                stack.append(tr)
                tr = tr.left
            else:
                tr = stack.pop()
                res.append(tr.val)
                tr = tr.right
        return res
