# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head

        while current is not None and current.next is not None:
            if current.next.val == current.val:
                #if the next value is not same to the current value, change the pointer looking at next to the one after
                current.next = current.next.next
            else:
                current = current.next

        return head