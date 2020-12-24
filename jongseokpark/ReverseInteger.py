import unittest


class Solution:
    @staticmethod
    def reverse_integer(x: int) -> int:
        input_number = str(x)
        if x == 0:
            return 0
        elif x < 0:
            return int(("-" + input_number[:0:-1]))
        else:
            return int(input_number[::-1])


class ReverseIntegerTest(unittest.TestCase):

    def test_reverse_integer_test(self):
        self.assertEqual(Solution().reverse_integer(123), 321)
        self.assertEqual(Solution().reverse_integer(-123), -321)
        self.assertEqual(Solution().reverse_integer(-1200), -21)
        self.assertEqual(Solution().reverse_integer(120), 21)
        self.assertEqual(Solution().reverse_integer(12000), 21)
        self.assertEqual(Solution().reverse_integer(1201), 1021)
        self.assertEqual(Solution().reverse_integer(0), 0)
        self.assertEqual(Solution().reverse_integer(1534236469), 9646324351)


if __name__ == '__main__':
    unittest.main()
