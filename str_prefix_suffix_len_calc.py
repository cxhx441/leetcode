"""
This is the pattern length calculation algorithm. It is used in Knuth Morris Pratt (KMP) for pattern matching.
https://www.youtube.com/watch?v=V5-7GzOfADQ&t=4s
https://www.youtube.com/watch?v=EL4ZbRF587g
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
"""
import unittest


def get_border_width(pattern: str) -> str:
    left = 0
    right = 1
    widths = [0] * len(pattern)

    while right < len(pattern):
        if pattern[left] == pattern[right]:
            left += 1
            widths[right] = left
            right += 1
        else:
            if left == 0:
                widths[right] = 0
                right += 1
            else:
                left = widths[left - 1]

    return "".join([str(x) for x in widths])


class testPatternLen(unittest.TestCase):
    def test1(self):
        self.assertEqual(get_border_width("abcdabeabf"), "0000120120")

    def test2(self):
        self.assertEqual(get_border_width("abcdeabfabc"), "00000120123")

    def test3(self):
        self.assertEqual(get_border_width("aabcadaabe"), "0100101230")

    def test4(self):
        self.assertEqual(get_border_width("aaaabaacd"), "012301200")

    def test5(self):
        self.assertEqual(get_border_width("abcxxxabcy"), "0000001230")

    def test6(self):
        self.assertEqual(get_border_width("abcaaabcac"), "0001112340")

    def test7(self):
        self.assertEqual(get_border_width("abcab__abcac"), "000120012340")


if __name__ == "__main__":
    unittest.main()
