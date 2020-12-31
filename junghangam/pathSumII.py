# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        import copy
        ret = []
        
        def dfs(curSum, curList,leftRoot):
            # print(curSum, curList, ret, leftRoot.val)
            if leftRoot.right == None and leftRoot.left == None:
                # print('here', leftRoot.val)
                if leftRoot.val + curSum == sum:
                    curList.append(leftRoot.val)
                    ret.append(curList)
            elif leftRoot.right == None:
                # print('there', leftRoot.val)
                #do left
                curSum += leftRoot.val
                curList.append(leftRoot.val)
                v = curList.copy()
                dfs(curSum, v, leftRoot.left)
            elif leftRoot.left == None:
                #do right
                curSum += leftRoot.val
                curList.append(leftRoot.val)
                x = curList.copy()
                dfs(curSum, x, leftRoot.right)
            else:
                #do dfs
                curSum += leftRoot.val
                curList.append(leftRoot.val)
                c = curList.copy()
                d = curList.copy()
                dfs(curSum, c, leftRoot.left)
                dfs(curSum, d, leftRoot.right)
        
            return ret

        if root == None:
            return []
        return dfs(0, [], root)
