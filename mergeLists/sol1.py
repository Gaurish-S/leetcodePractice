# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curList2 = 0
        for i in list1:
            # iterate until you find a place to slot i into into list2
            while curList2 < len(list2) and not ( i >= list2[curList2] and i <= list2[curList2 + 1]):
                curList2 = curList2 + 1
            if curList2 


