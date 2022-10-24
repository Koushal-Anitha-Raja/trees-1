#TC:O(n)
#SC:O(H)+O(n)= O(n)#as we are using recursive stack O(H) , H is height of tree, as n is dominating term  

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        
        
        #without using the list array
        
        #setting a flag variable
        self.flag=True
        #declaring a previous variable
        self.prev=float("-Inf")
        self.inorder(root)
        #fina;;y returning the flag value
        return self.flag
    
        #BST approach
    def inorder(self,root):
        #base condition
        if root==None:
            #if it hits the base the function will unfold
            return
        
        #logic
        #moving to left child of root node
        self.inorder(root.left)
        
        #if the prev value is not lesser than current value
        if not (self.prev<root.val):
            self.flag=False
            #then again changing the previous value to current root value
        self.prev=root.val
        
        
        #moving to the right child of node root
        self.inorder(root.right)
        
        