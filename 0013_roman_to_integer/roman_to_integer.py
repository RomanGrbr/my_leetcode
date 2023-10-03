ROMAN = {
    'I': 1,
    'V': 5,
    'S': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}


class Solution:
    def romanToInt(self, s: str) -> int:
        # result = 0
        # s_list = list(s)
        # if len(s) <= 1:
        #     return ROMAN[s]
        # for i in range(1, len(s)):
        #     if s_list[i - 1] < s_list[i]:
        #         result += ROMAN[s_list[i]] - ROMAN[s_list[i - 1]]
        #     else:
        #         result += ROMAN[s_list[i - 1]]
        #         if i == len(s) - 1:
        #             result += ROMAN[s_list[i]]
        # return result
        result = 0
        numbers = list(s)

        for i in range(len(numbers)):
            try:
                print(ROMAN[numbers[i]])
                if ROMAN[numbers[i]] <= ROMAN[numbers[i + 1]]:
                    result += ROMAN[numbers[i]]
                else:
                    result += ROMAN[numbers[i + 1]] - ROMAN[numbers[i]]
            except IndexError:
                result += ROMAN[numbers[-1]]
        return result


if __name__ == '__main__':
    result = Solution()
    print(result.romanToInt('LVIII'))
