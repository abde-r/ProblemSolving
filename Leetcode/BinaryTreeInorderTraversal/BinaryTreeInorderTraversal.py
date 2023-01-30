# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        t = []
        def helperFun(root):
            if not root:
                return None
            helperFun(root.left)
            t.append(root.val)
            helperFun(root.right)
        helperFun(root)
        return t

