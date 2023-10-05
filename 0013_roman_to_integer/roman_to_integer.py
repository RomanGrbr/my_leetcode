ROMAN = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}


class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        index = 1
        len_s = len(s)
        if len_s == 1:
            return ROMAN[s]
        while index < len_s:
            if ROMAN[s[index - 1]] >= ROMAN[s[index]]:
                result += ROMAN[s[index - 1]]
                index += 1
            else:
                result += ROMAN[s[index]] - ROMAN[s[index - 1]]
                index += 2
        if index == len_s:
            result += ROMAN[s[index - 1]]
            return result
        return result


if __name__ == '__main__':
    result = Solution()
    print(result.romanToInt("MDCXCV"))  # 1695
    print(result.romanToInt("III"))  # 3
    print(result.romanToInt("XIV"))  # 14
    print(result.romanToInt("MCMXCIV"))  # 1994
