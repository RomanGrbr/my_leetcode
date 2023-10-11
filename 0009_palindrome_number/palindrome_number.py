class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = list(str(x))
        return y == y[::-1]


def my_revers(x: list):
    for i in range(len(x)):
        if i <= len(x) // 2:
            if x[i] != x[len(x) - i - 1]:
                return False
    return True


if __name__ == '__main__':
    # x = 12321
    # result = Solution()
    # print(result.isPalindrome(x))
    x = [1, 2, 2, 2, 1]
    print(my_revers(x))
