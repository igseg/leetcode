# 2. Add Two Numbers
# Medium

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        head    = ListNode(0)
        current = head

        carry = 0

        while True:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            carry, value = divmod(val1+val2+ carry, 10)
            current.val = value

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            if l1 == None and l2==None and carry == 0:
                break

            current.next = ListNode(0)
            current = current.next

        return head
