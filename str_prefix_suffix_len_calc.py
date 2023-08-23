"""
This is the pattern length calculation algorithm. It is used in Knuth Morris Pratt (KMP) for pattern matching.
https://www.youtube.com/watch?v=V5-7GzOfADQ&t=4s
https://www.youtube.com/watch?v=EL4ZbRF587g
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
"""
import unittest


def pattern_len(pattern: str) -> str:
    left = 0
    right = 1
    lengths = [0] * len(pattern)

    while right < len(pattern):
        if pattern[left] == pattern[right]:
            lengths[right] = lengths[right - 1] + 1
            left += 1
        else:
            lengths[right] = 0
            left = 0
        right += 1

    return "".join([str(x) for x in lengths])


class testPatternLen(unittest.TestCase):
    def test1(self):
        self.assertEqual(pattern_len("abcdabeabf"), "0000120120")

    def test2(self):
        self.assertEqual(pattern_len("abcdeabfabc"), "00000120123")

    def test3(self):
        self.assertEqual(pattern_len("aabcadaabe"), "0100101230")

    def test4(self):
        self.assertEqual(pattern_len("aaaabaacd"), "012301200")

    def test5(self):
        self.assertEqual(pattern_len("abcxxxabcy"), "0000001230")


if __name__ == "__main__":
    unittest.main()
