# coding=utf-8

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def dfs(root, res):
    if root is None: return 
    if root.left:
        dfs(root.left, res)
    res.append(root.val)
    if root.right:
        dfs(root.right, res)

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        dfs(root, res)
        return res
