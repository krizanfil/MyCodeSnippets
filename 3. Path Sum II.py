from typing import Optional, List


class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def pathSum(root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

    result = []

    if not root:
        return []

    def dfs(node: TreeNode, path: List[int], cur_sum: int) -> None:
        cur_sum += node.val
        cur_path = path + [node.val]

        if node.left:
            dfs(node.left, cur_path, cur_sum)
        if node.right:
            dfs(node.right, cur_path, cur_sum)
        if not node.left and not node.right and cur_sum == targetSum:
            result.append(cur_path)

    dfs(root, [], 0)
    return result
