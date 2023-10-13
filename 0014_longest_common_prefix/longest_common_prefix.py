from typing import List


# class Solution:
#     """Поиск строки в подстроке"""
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         if len(strs) <= 1:
#             return strs[0]
#         min = strs[0]
#         for word in strs[1:]:
#             if len(min) > len(word):
#                 min = word
#         strs.remove(min)
#         i = len(min)
#         while i != 0:
#             flag = True
#             for j in range(len(min) + 1 - i):
#                 prefix = min[j:j+i]
#                 for word in strs:
#                     if prefix not in word:
#                         flag = False
#                 if flag:
#                     return prefix
#             i -= 1
#         return ''

class Solution:
    """Поиск самого длинного префикса в списке строк"""
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min = strs[0]
        for word in strs[1:]:
            if len(min) > len(word):
                min = word
        strs.remove(min)
        i = len(min)
        while i != 0:
            flag = True
            for word in strs:
                if min[0:i] not in word[0:i]:
                    flag = False
                    break
            if flag:
                return min[0:i]
            i -= 1
        return ''


if __name__ == '__main__':
    # x = ["reflower", "flow", "flight"]
    x = ["flower", "flow", "flight"]
    # x = ["dog", "racecar", "car"]
    result = Solution()
    print(result.longestCommonPrefix(x))  # "fl"
