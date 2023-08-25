from pointer_debug import pointer_debug


def str_matching_kmp(needle: str, haystack: str) -> int:
    """
    Return the starting index of the str to be found (needle) within the (haystack)
    Else return -1
    """
    # m = len(haystack)
    # n = len(needle)

    ## brute-force
    # traverse haystack, at each element, check if needle starts at that index. O(mn)

    ## KMP
    # generate a list of len(needle), using greedy algorithm, where each index, corresponds to the
    # max proper shared suffix/prefix (border) length (width) -> border_width
    def get_border_width(pattern: str) -> list:  # O(n) algo in this context
        """
        This is the pattern length calculation algorithm. It is used in Knuth Morris Pratt (KMP) for pattern matching.
        https://www.youtube.com/watch?v=V5-7GzOfADQ&t=4s
        https://www.youtube.com/watch?v=EL4ZbRF587g
        https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

        example:
        "abcaaabcac"
        "0001112340"
        """
        border_widths = [0] * len(pattern)

        l, r = 0, 1
        while r < len(pattern):
            if pattern[l] == pattern[r]:
                l += 1
                border_widths[r] = l
                r += 1
            else:
                if l == 0:
                    border_widths[r] = 0
                    r += 1
                else:
                    l = border_widths[l - 1]

        return border_widths

    border_widths = get_border_width(needle) + [0]
    # now use the second half of kmp to find the substring index in O(m)
    i, j = 0, -1
    while i < len(haystack):
        pointer_debug(haystack, {i: ["i"]})
        pointer_debug(needle, {j: ["j"]})
        if j == len(needle) - 1:
            return i - j - 1

        if haystack[i] == needle[j + 1]:
            j += 1
            i += 1
        else:
            if j != -1:
                j = border_widths[j] - 1
            else:
                i += 1

    if j == len(needle) - 1:
        return i - j - 1

    return -1  # O(m + n)


def str_matching_rabin_karp(needle: str, haystack: str) -> int:
    BASE = 26  # number of possible unique chars in haystack U needle

    def get_pattern_hash(pattern: str) -> int:
        pattern_hash = 0
        for i, ch in enumerate(pattern):
            power = len(pattern) - i - 1
            pattern_hash += ord(ch) * BASE**power
        return pattern_hash

    needle_hash = get_pattern_hash(needle)
    l, r = 0, len(needle)
    haystack_window_hash = get_pattern_hash(haystack[:r])
    while r < len(haystack):
        if needle_hash == haystack_window_hash and needle == haystack[l:r]:
            return l

        # update haystack hash
        haystack_window_hash -= ord(haystack[l]) * BASE ** (len(needle) - 1)
        haystack_window_hash *= 26
        haystack_window_hash += ord(haystack[r])

        l += 1
        r += 1

    if needle_hash == haystack_window_hash and needle == haystack[l:r]:
        return l

    return -1
