import unittest


class Solution:
    @staticmethod
    def roman_to_integer(s: str) -> int:
        roman_to_integer_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        s = s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC")
        result = 0
        for roman in s:
            result += roman_to_integer_dict[roman]
        return result


class RomanToIntegerTest(unittest.TestCase):

    def test_reverse_integer_test(self):
        self.assertEqual(Solution().roman_to_integer("III"), 3)
        self.assertEqual(Solution().roman_to_integer("IV"), 4)
        self.assertEqual(Solution().roman_to_integer("IX"), 9)
        self.assertEqual(Solution().roman_to_integer("LVIII"), 58)
        self.assertEqual(Solution().roman_to_integer("MCMXCIV"), 1994)


if __name__ == '__main__':
    unittest.main()
