import unittest
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if target == (nums[i] + nums[j]):
                    return [i, j]

        # temp = {}
        # for index, value in enumerate(nums):
        #     find_number = target - value
        #     if find_number in temp:
        #         return [temp[find_number], index]
        #     else:
        #         temp[value] = index


class TwoSumTest(unittest.TestCase):

    def test_two_sum(self):
        self.assertListEqual(Solution().twoSum([2, 7, 11, 15], 9), [0, 1])
        self.assertListEqual(Solution().twoSum([3, 2, 4], 6), [1, 2])
        self.assertListEqual(Solution().twoSum([3, 3], 6), [0, 1])


if __name__ == '__main__':
    unittest.main()
