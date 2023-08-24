import unittest


def str_matching(needle: str, haystack: str) -> int:
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
    def get_border_width(pattern: str) -> str: # O(n) algo in this context
        """
        example:
        "abcaaabcac"
        "0001112340"
        """
        border_widths = [0]*len(pattern)

        left, right = 0, 1
        while right < len(pattern):
            if pattern[left] == pattern[right]:
                left += 1
                border_widths[right] = left
                right += 1
            else:
                if left == 0:
                    border_widths[right] = 0
                    right += 1
                else:
                    left = border_widths[left - 1]

        return ''.join([str(x) for x in border_widths])

    # now use the second half of kmp to jump around. 




    return -1

class TestStrMatching(unittest.TestCase):
    def test_1(self):
        self.assertEqual(str_matching("howww", "01234howww"), 5)

    def test_2(self):
        self.assertEqual(str_matching("howww", "howww01234"), 0)

    def test_3(self):
        self.assertEqual(str_matching("h", "0123h567"), 4)

    def test_4(self):
        self.assertEqual(str_matching("how", "01234"), -1)

    def test_5(self):
        self.assertEqual(str_matching("h", "012"), 3)

    def test_6(self):
        self.assertEqual(str_matching("h", "h01234"), 0)

    def test_7(self):
        self.assertEqual(str_matching("h", "012h45"), 3)


if __name__ == "__main__":
    unittest.main()
