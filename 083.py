# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head):
        result_array = []
        val = head.val
        while val:
            if val not in result_array:
                result_array.append(val)
            if head.next:
                head = head.next
                val = head.val
            else:
                break
        return result_array


## TESTCASE 1 ##
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
l1 = ListNode(2)
l2 = ListNode(1, l1)
l3 = ListNode(1, l2)

s = Solution()

result = s.deleteDuplicates(l3)
try:
    print(result)
    assert result == [1, 2]
except AssertionError:
    print("TEST 1 Error")
else:
    print("TEST 1 ok")


## Attention, not working in leetcode