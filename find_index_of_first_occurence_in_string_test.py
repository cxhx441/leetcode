import unittest
from find_index_of_first_occurence_in_string import str_matching

class TestStrMatching(unittest.TestCase):
    def test_1(self):
        """Needle is multi char at end of haystack"""
        self.assertEqual(str_matching("hhoww", "01234hhoww"), 5)

    def test_2(self):
        """Needle is multi char at beginning of haystack"""
        self.assertEqual(str_matching("hhoww", "hhoww01234"), 0)

    def test_3(self):
        """Needle is multi char in middle of haystack"""
        self.assertEqual(str_matching("h", "0123h567"), 4)

    def test_4(self):
        """Needle is multi char not in haystack"""
        self.assertEqual(str_matching("hhhasdfow", "0123asdfasdfasdf4"), -1)

    def test_5(self):
        """Needle is single char not in haystack"""
        self.assertEqual(str_matching("h", "012"), -1)

    def test_6(self):
        """Needle is single char at beginning of haystack"""
        self.assertEqual(str_matching("h", "h01234"), 0)

    def test_7(self):
        """Needle is single char in middle of haystack"""
        self.assertEqual(str_matching("h", "012h45"), 3)

    def test_8(self):
        """Needle is single char in end of haystack"""
        self.assertEqual(str_matching("h", "012345h"), 6)

    def test_9(self):
        """Needle is larger than Haystack"""
        self.assertEqual(str_matching("hasdfasdf", "012"), -1)

    def test_10(self):
        self.assertEqual(str_matching("issip", "mississippi"), 4)


if __name__ == "__main__":
    unittest.main()
