"""
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
"""

def rightSideView(self, root: TreeNode) -> List[int]:
        queue, result = [], []
        if root == None:
            return
        queue.append(root)
        level = []
        while queue:
            size = len(queue)
            for i in range(len(queue)):
                root = queue.pop(0)
                if i == size - 1:
                    result.append(root.val)
                if root.left:
                    queue.append(root.left, )
                if root.right:
                    queue.append(root.right)
        
        return result
