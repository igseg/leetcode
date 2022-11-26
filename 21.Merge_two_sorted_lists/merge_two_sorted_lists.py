# 21. Merge Two Sorted Lists

# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 == None and list2 == None:
            return None

        head    = ListNode(0)
        current = head

        while list1 != None:
            if list2 == None:
                current.val  = list1.val
                list1        = list1.next

            elif list2.val < list1.val:
                current.val  = list2.val
                list2        = list2.next

            else:
                current.val  = list1.val
                list1        = list1.next

            if list1 == None and list2 == None:
                continue

            current.next = ListNode(0)
            current = current.next


        while list2 != None:
            current.val  = list2.val
            list2        = list2.next
            if list2 != None:
                current.next = ListNode(0)
                current = current.next


        return head
