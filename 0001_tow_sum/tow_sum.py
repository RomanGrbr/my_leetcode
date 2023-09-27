from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for first in range(len(nums)):
            for second in range(first, len(nums)):
                if first < second and nums[first] + nums[second] == target:
                    return [first, second]


if __name__ == '__main__':
    result = Solution()
    print(result.twoSum([3, 2, 3], 6))
