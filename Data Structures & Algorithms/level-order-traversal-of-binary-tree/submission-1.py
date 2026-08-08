# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque()
        q.append(root)
        res = []
        while q:
            level_values = []
            level_size = len(q)
            for _ in range(level_size):
                node = q.popleft()
                level_values.append(node.val)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)
            res.append(level_values)
        return res