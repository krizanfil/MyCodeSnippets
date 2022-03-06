from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    levels = []

    queue = []
    queue.append(root)

    while queue:
        q_length = len(queue)
        cur_level = []

        for i in range(q_length):
            node = queue.pop(0)
            if node:
                cur_level.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
        if cur_level:
            levels.append(cur_level)

    return levels
