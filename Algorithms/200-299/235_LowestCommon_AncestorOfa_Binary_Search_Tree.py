# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        node = root
        while node:
            if min(p.val, q.val) <= node.val and max(p.val, q.val) >= node.val:
                return node.val
            if max(p.val, q.val) < node.val:
                node = node.left
            if min(p.val, q.val) > node.val:
                node = node.right
        
