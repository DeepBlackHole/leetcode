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

# Solution

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
## Explanation from ChatGPT
# Merge Two Sorted Linked Lists — Plain-English Walk-Through

> **Goal**
> Combine two **already-sorted** singly linked lists into one sorted list without creating extra nodes.

---

## 1. Building Blocks (`ListNode`)

```python
from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next: 'Optional[ListNode]' = None):
        self.val  = val   # value stored in this node
        self.next = next  # pointer to the next node (or None if it’s the tail)
```

Think of each `ListNode` as a train car:

| Field  | Meaning              |
| ------ | -------------------- |
| `val`  | Number on the car    |
| `next` | Link to the next car |

---

## 2. The `mergeTwoLists` Method

```python
class Solution:
    def mergeTwoLists(
        self, 
        list1: Optional[ListNode], 
        list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        dummy = ListNode()      # empty “front car” so we never lose the head
        tail  = dummy           # tail always follows the last sorted node

        while list1 and list2:  # loop until one list runs out
            if list1.val < list2.val:
                tail.next = list1   # attach the smaller node
                list1 = list1.next  # advance in list1
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next        # move the tail pointer forward

        # One list might still have nodes left — attach them all at once
        tail.next = list1 if list1 else list2

        return dummy.next  # skip the dummy and return the real head
```

### Why it works

1. **Dummy node**
   Saves us from special-casing the very first insertion.
2. **Tail pointer**
   Always marks the end of the merged list so we can append in O(1).
3. **Greedy pick**
   Each loop chooses the smaller current value, preserving sorted order.

### Time & Space Complexity

| Metric | Cost         | Reason                                 |
| ------ | ------------ | -------------------------------------- |
| Time   | **O(m + n)** | Touches every node exactly once        |
| Memory | **O(1)**     | Only a few pointers, no new list nodes |

---

## 3. Helper `print_list`

```python
def print_list(head: ListNode) -> None:
    cur = head
    while cur:
        print(cur.val, end=" ")
        cur = cur.next
```

---

## 4. End-to-End Example

```python
# Build two lists: [1, 2, 4] and [1, 3, 4]
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

merged_head = Solution().mergeTwoLists(list1, list2)
print_list(merged_head)       # ➜ 1 1 2 3 4 4
```

---

## 5. Common Pitfall

```python
print_list(merged_listfdl)  # NameError: merged_listfdl is undefined
```

Should be:

```python
print_list(merged_head)
```

---

## Explanation from gemini

It looks like there's a small typo in your example usage where you have `merged_listfdl` instead of `merged_list` when calling `print_list`. I'll explain the provided Python code assuming that's corrected.

-----

## Explanation of the Code: Merging Two Sorted Linked Lists

The provided code implements a solution to merge two sorted linked lists into a single, sorted linked list. Let's break down each part:

-----

### 1\. `ListNode` Class

This class defines the structure of a **node** in a linked list.

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

  * `__init__(self, val=0, next=None)`: This is the constructor for the `ListNode`.
      * `val`: Stores the actual data (value) of the node. It defaults to `0`.
      * `next`: A pointer (or reference) to the next node in the list. It defaults to `None`, indicating the end of a list or sublist.

-----

### 2\. `Solution` Class and `mergeTwoLists` Method

This class contains the core logic for merging the linked lists.

```python
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
```

  * `mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]`: This method takes two sorted linked lists (`list1` and `list2`) as input and returns a new sorted linked list.
      * `dummy = ListNode()`: A **dummy node** is created. This is a common technique used to simplify the logic of adding elements to the beginning of a new linked list. Instead of handling a special case for the first node, you can always append to `dummy.next`.
      * `tail = dummy`: A `tail` pointer is initialized to the dummy node. This `tail` pointer will always point to the **last node of our merged list** (or the dummy node if the list is empty), allowing us to easily append new nodes.
      * `while list1 and list2:`: This loop continues as long as both `list1` and `list2` have nodes remaining.
          * `if list1.val < list2.val:`: It compares the values of the current nodes in `list1` and `list2`.
              * If the value in `list1` is smaller, `tail.next` is set to `list1`, effectively appending the current node from `list1` to our merged list. Then, `list1` is advanced to its next node (`list1 = list1.next`).
          * `else:`: If the value in `list2` is smaller or equal.
              * `tail.next` is set to `list2`, appending the current node from `list2` to our merged list. Then, `list2` is advanced to its next node (`list2 = list2.next`).
          * `tail = tail.next`: In both cases, after appending a node, the `tail` pointer is moved to the newly added node.
      * `tail.next = list1 if list1 else list2`: After the `while` loop finishes, one of the lists might still have remaining elements (because the other list became `None`). This line appends all remaining nodes from the non-empty list to the end of our merged list. Since both input lists were already sorted, any remaining nodes will also be in sorted order.
      * `return dummy.next`: Finally, the method returns `dummy.next`, which is the head of the newly merged sorted linked list (skipping the dummy node itself).

-----

### 3\. `print_list` Function

This utility function helps visualize the linked list.

```python
def print_list(head: ListNode) -> None:
    cur = head
    while cur:
        print(cur.val, end=" ")
        cur = cur.next
```

  * `print_list(head: ListNode) -> None`: Takes the head of a linked list as input and prints its values.
      * `cur = head`: A `cur` pointer is initialized to the head of the list.
      * `while cur:`: The loop continues as long as `cur` is not `None` (i.e., there are still nodes to print).
      * `print(cur.val, end=" ")`: Prints the value of the current node, followed by a space instead of a newline, so all values are on the same line.
      * `cur = cur.next`: Moves `cur` to the next node in the list.

-----

### 4\. Example Usage

This section demonstrates how to use the above classes and function.

```python
# Example usage:
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
sol = Solution()
merged_list = sol.mergeTwoLists(list1, list2)

# Print the merged linked list
print_list(merged_list) # Corrected from merged_listfdl
```

  * `list1 = ListNode(1, ListNode(2, ListNode(4)))`: Creates the first linked list: `1 -> 2 -> 4`.
  * `list2 = ListNode(1, ListNode(3, ListNode(4)))`: Creates the second linked list: `1 -> 3 -> 4`.
  * `sol = Solution()`: Creates an instance of the `Solution` class.
  * `merged_list = sol.mergeTwoLists(list1, list2)`: Calls the `mergeTwoLists` method to merge `list1` and `list2`, storing the head of the merged list in `merged_list`.
  * `print_list(merged_list)`: Prints the values of the merged linked list.

When you run this code, the output will be: ` 1 1 2 3 4 4  ` which is the sorted merge of the two input lists.

-----

This solution is efficient as it only requires a single pass through both linked lists, making its time complexity **O(N + M)**, where N and M are the lengths of `list1` and `list2` respectively. The space complexity is **O(1)** because it only uses a few extra pointers and doesn't create new nodes for the values themselves, just re-arranges the existing ones.
