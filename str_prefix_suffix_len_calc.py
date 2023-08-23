"""
This is the pattern length calculation algorithm. It is used in Knuth Morris Pratt (KMP) for pattern matching. 
https://www.youtube.com/watch?v=V5-7GzOfADQ&t=4s
https://www.youtube.com/watch?v=EL4ZbRF587g
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
"""
import unittest

def pattern_len(pattern: str) -> list:
    left = 0
    right = 1
    lengths = [0]*len(pattern)

    while right < len(pattern):
        if pattern[left] == pattern[right]:
            lengths[right] = lengths[right-1] + 1
            left += 1
        else:
            lengths[right] = 0
            left = 0
        right += 1

    return lengths


class testPatternLen(unittest.TestCase):
    def test1(self):
        pattern = "abcdabeabf"
        expected = [int(x) for x in "0000120120"]
        print(pattern_len(pattern))
        self.assertEqual(pattern_len(pattern), expected)

    def test2(self):
        pattern = "abcdeabfabc"
        expected = [int(x) for x in "00000120123"]
        print(pattern_len(pattern))
        self.assertEqual(pattern_len(pattern), expected)

    def test3(self):
        pattern = "aabcadaabe"
        expected = [int(x) for x in "0100101230"]
        print(pattern_len(pattern))
        self.assertEqual(pattern_len(pattern), expected)

    def test4(self):
        pattern = "aaaabaacd"
        expected = [int(x) for x in "012301200"]
        print(pattern_len(pattern))
        self.assertEqual(pattern_len(pattern), expected)

    def test5(self):
        pattern = "abcxxxabcy"
        expected = [int(x) for x in "0000001230"]
        print(pattern_len(pattern))
        self.assertEqual(pattern_len(pattern), expected)

if __name__ == "__main__":
    unittest.main()
