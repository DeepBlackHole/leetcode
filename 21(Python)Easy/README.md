# 21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.![alt text](image.png)

## Examples

### Example 1

| Input: list1 = [1,2,4], list2 = [1,3,4]

Output: [1,1,2,3,4,4]

### Example 2

| Input: list1 = [], list2 = []

Output: []

### Example 3

| Input: list1 = [], list2 = [0]

Output: [0]

```python
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
print_list(merged_listfdl)
```
