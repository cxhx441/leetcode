import unittest
from find_index_of_first_occurence_in_string import str_matching_kmp, str_matching_rabin_karp


class TestStrMatchingKMP(unittest.TestCase):
    def test_1(self):
        """Needle is multi char at end of haystack"""
        self.assertEqual(str_matching_kmp("hhoww", "01234hhoww"), 5)

    def test_2(self):
        """Needle is multi char at beginning of haystack"""
        self.assertEqual(str_matching_kmp("hhoww", "hhoww01234"), 0)

    def test_3(self):
        """Needle is multi char in middle of haystack"""
        self.assertEqual(str_matching_kmp("h", "0123h567"), 4)

    def test_4(self):
        """Needle is multi char not in haystack"""
        self.assertEqual(str_matching_kmp("hhhasdfow", "0123asdfasdfasdf4"), -1)

    def test_5(self):
        """Needle is single char not in haystack"""
        self.assertEqual(str_matching_kmp("h", "012"), -1)

    def test_6(self):
        """Needle is single char at beginning of haystack"""
        self.assertEqual(str_matching_kmp("h", "h01234"), 0)

    def test_7(self):
        """Needle is single char in middle of haystack"""
        self.assertEqual(str_matching_kmp("h", "012h45"), 3)

    def test_8(self):
        """Needle is single char in end of haystack"""
        self.assertEqual(str_matching_kmp("h", "012345h"), 6)

    def test_9(self):
        """Needle is larger than Haystack"""
        self.assertEqual(str_matching_kmp("hasdfasdf", "012"), -1)

    def test_10(self):
        self.assertEqual(str_matching_kmp("issip", "mississippi"), 4)

    def test_11(self):
        self.assertEqual(str_matching_kmp("sad", "sadbutsad"), 0)

    def test_12(self):
        self.assertEqual(str_matching_kmp("leeto", "leetcode"), -1)

class TestStrMatchingRabinKarp(unittest.TestCase):
    def test_1(self):
        """Needle is multi char at end of haystack"""
        self.assertEqual(str_matching_rabin_karp("hhoww", "01234hhoww"), 5)

    def test_2(self):
        """Needle is multi char at beginning of haystack"""
        self.assertEqual(str_matching_rabin_karp("hhoww", "hhoww01234"), 0)

    def test_3(self):
        """Needle is multi char in middle of haystack"""
        self.assertEqual(str_matching_rabin_karp("h", "0123h567"), 4)

    def test_4(self):
        """Needle is multi char not in haystack"""
        self.assertEqual(str_matching_rabin_karp("hhhasdfow", "0123asdfasdfasdf4"), -1)

    def test_5(self):
        """Needle is single char not in haystack"""
        self.assertEqual(str_matching_rabin_karp("h", "012"), -1)

    def test_6(self):
        """Needle is single char at beginning of haystack"""
        self.assertEqual(str_matching_rabin_karp("h", "h01234"), 0)

    def test_7(self):
        """Needle is single char in middle of haystack"""
        self.assertEqual(str_matching_rabin_karp("h", "012h45"), 3)

    def test_8(self):
        """Needle is single char in end of haystack"""
        self.assertEqual(str_matching_rabin_karp("h", "012345h"), 6)

    def test_9(self):
        """Needle is larger than Haystack"""
        self.assertEqual(str_matching_rabin_karp("hasdfasdf", "012"), -1)

    def test_10(self):
        self.assertEqual(str_matching_rabin_karp("issip", "mississippi"), 4)

    def test_11(self):
        self.assertEqual(str_matching_rabin_karp("sad", "sadbutsad"), 0)

    def test_12(self):
        self.assertEqual(str_matching_rabin_karp("leeto", "leetcode"), -1)

if __name__ == "__main__":
    unittest.main()
