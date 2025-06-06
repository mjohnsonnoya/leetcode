# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        traversal = []
        if not root:
            return []
        q.append(root)
        while q:
            num_nodes = len(q)
            level = []
            for _ in range(num_nodes):
                node = q.popleft()
                level.append(node.val)
                l, r = node.left, node.right
                if l:
                    q.append(l)
                if r:
                    q.append(r)
            traversal.append(level)
        return traversal

