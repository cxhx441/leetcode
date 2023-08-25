import unittest
from get_border_width import get_border_width


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

    def test8(self):
        self.assertEqual(get_border_width("abcaaabdac"), "0001112010")


if __name__ == "__main__":
    unittest.main()
