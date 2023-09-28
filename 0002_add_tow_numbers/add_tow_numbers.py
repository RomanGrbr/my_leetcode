from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        pass


        # if len(l1) < len(l2):
        #     l1, l2 = l2, l1
        # for i in range(len(l1)):
        #     if i < len(l2):
        #         new_mind = (l1[i] + l2[i] + mind) % TEN
        #         result.append(new_mind)
        #         mind = (l1[i] + l2[i] + mind) // TEN
        #     else:
        #         new_mind = (l1[i] + mind) % TEN
        #         result.append(new_mind)
        #         mind = (l1[i] + mind) // TEN
        # if mind > 0:
        #     result.append(mind)

        return result


if __name__ == '__main__':
    # first = [2, 4, 3]
    # second = [5, 6, 4]
    # first = [9, 9, 9, 9]
    # second = [9]
    first = [9]
    second = [9, 9, 9, 9]
    result = Solution()
    print(result.addTwoNumbers(first, second))
