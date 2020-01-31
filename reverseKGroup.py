"""
Problem Description

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.

"""

def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        current = head
        count = 0
        while current and count != k:
            current = current.next
            count += 1
        if count == k:
            current = self.reverseKGroup(current, k)
            while count > 0:
                ahead = head.next
                head.next = current
                current = head
                head = ahead
                count -= 1
            return current
        else:
            return head
