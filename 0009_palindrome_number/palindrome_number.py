class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = list(str(x))
        return y == y[::-1]


if __name__ == '__main__':
    x = 121
    result = Solution()
    print(result.isPalindrome(x))
