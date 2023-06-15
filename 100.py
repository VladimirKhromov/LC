# Definition for a binary tree node.
# If both trees reach their end, then every node in them was checked (return True)
# If one tree ends before the other (return False)
# If a node is different than another (return False)
# Call the function to check the left & right subtrees
# return their conjunction (AND)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# If both trees reach their end, then every node in them was checked (return True)
# If one tree ends before the other (return False)
# If a node is different than another (return False)
# Call the function to check the left & right subtrees
# return their conjunction (AND)
        
class Solution(object):
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None: 
            return True
        if p == None or q == None:
            return False
        if p.val != q.val: 
            return False
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)