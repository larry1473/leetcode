# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        if(root == None):
            return res
        self.helper(root,res,"")
        return res
    def helper(self,root,arr,path):
        if root == None:
            return 
        elif(root.left == None and root.right == None):
            arr.append(path+str(root.val))
            return
        self.helper(root.left,arr,path+str(root.val)+ "->")
        self.helper(root.right,arr,path+str(root.val)+ "->")
        

       
            

        