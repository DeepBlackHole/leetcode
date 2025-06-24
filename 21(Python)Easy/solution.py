from typing import Optional  
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode() 
        tail = dummy       

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        tail.next = list1 if list1 else list2
        return dummy.next 
def print_list(head: ListNode) -> None:
    cur = head
    while cur:
        print(cur.val, end=" ")
        cur = cur.next


# Example usage:
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
sol = Solution()
merged_list = sol.mergeTwoLists(list1, list2)   


# Print the merged linked list
print_list(merged_list)