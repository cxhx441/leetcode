# https://leetcode.com/problems/subtree-of-another-tree/
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_subtree(root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
    # serialization method
    def serialize_tree(serial_root) -> str:
        """
        Serialize the tree using pre-order traversal.
        Can be done using post-order traversal.
        Not using in-order traversal because it is not unique.
        """
        serialized_list = []
        stack = [serial_root]
        while stack:
            cur_node = stack.pop()
            serialized_list.append("^")
            if cur_node is None:
                serialized_list.append("#")
            else:
                serialized_list.append(str(cur_node.val))
                stack.append(cur_node.right)
                stack.append(cur_node.left)
        return "".join(serialized_list)

    root_serial = serialize_tree(root)
    subroot_serial = serialize_tree(subroot)

    # now it is just string matching
    if len(subroot_serial) > len(root_serial):
        return False

    for l in range(len(root_serial)):
        for r in range(len(subroot_serial)):
            if l + r >= len(root_serial) or root_serial[l + r] != subroot_serial[r]:
                break
            if root_serial[l + r] == subroot_serial[r] and r == len(subroot_serial) - 1:
                return True
    return False
