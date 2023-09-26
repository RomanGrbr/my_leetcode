from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        first: int = 0
        while first < len(nums) - 1:
            for second in range(first + 1, len(nums)):
                if nums[first] + nums[second] == target:
                    return [first, second]
            first += 1


if __name__ == '__main__':
    result = Solution()
    print(result.twoSum([3, 2, 3], 6))
