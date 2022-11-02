# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#Time_Compolexity: O(n)
#Space_Complexity: O(n)

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        #declaring a result array
        self.result=[]
        self.inorder(root)
        #iterate the result array to find the value is sorted 
        for i in range (1,len(self.result)):
            #if it is sorted then it is valid bst 
            if self.result[i-1]<self.result[i]:
                pass
            else:
                #return false if it is not sorted
                return False
        return True
        
        #BST approach
    def inorder(self,root):
        #base condition
        if root==None:
            #if it hits the base the function will unfold
            return
        
        #logic
        #moving to left child of root node
        self.inorder(root.left)
        #result will hold the value of specific node
        self.result.append(root.val)
        #moving to the right child of node root
        self.inorder(root.right)
        
