"""
This is the pattern length calculation algorithm. It is used in Knuth Morris Pratt (KMP) for pattern matching.
https://www.youtube.com/watch?v=V5-7GzOfADQ&t=4s
https://www.youtube.com/watch?v=EL4ZbRF587g
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
"""
from pointer_debug import pointer_debug


def get_border_width(pattern: str) -> str:
    border_widths = [0] * len(pattern)

    left, right = 0, 1
    while right < len(pattern):
        # pointer_debug(pattern, {left: ["l"], right: ["r"]})
        if pattern[left] == pattern[right]:
            left += 1
            border_widths[right] = left
            right += 1
        elif left == 0:
            border_widths[right] = 0
            right += 1
        else:
            left = border_widths[left - 1]

    return "".join([str(x) for x in border_widths])


