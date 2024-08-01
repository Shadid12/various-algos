# https://neetcode.io/problems/depth-of-binary-tree
#  Find Maximum Depth of Binary Tree

# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def maxDepth(self, root: Optional[TreeNode]) -> int:
    
    def dfs(node):
      if not node:
        return 0
      
      left = dfs(node.left)
      right = dfs(node.right)

      max_depth = max(left, right) + 1
      return max_depth
    
    return dfs(root)
  
# Helpers 
def build_tree(nodes: List[Optional[int]]) -> Optional[TreeNode]:
    if not nodes:
        return None

    root = TreeNode(nodes[0])
    queue = [root]
    i = 1

    while queue and i < len(nodes):
        current = queue.pop(0)
        if current:
            if i < len(nodes) and nodes[i] is not None:
                current.left = TreeNode(nodes[i])
                queue.append(current.left)
            i += 1
            if i < len(nodes) and nodes[i] is not None:
                current.right = TreeNode(nodes[i])
                queue.append(current.right)
            i += 1

    return root
    

# Todo: Turn [1,2,3,None,None,4] into a binary tree using the TreeNode class

# Test
l = Solution()
# Turn the list into a binary tree
#       1
#      / \
#     2   3
#        / \
#       4   5

r = l.maxDepth(build_tree([1,2,3,None,None,4]))
print(r) # 3

