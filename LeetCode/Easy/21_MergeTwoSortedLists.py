# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def mergeTwoLists(self, l1, l2):
        if l1.val > l2.val:
            l3 = ListNode(l2.val)
            l2 = l2.next
        else:
            l3 = ListNode(l1.val)
            l1 = l1.next

        l3Start = l3

        while True:
            if l1 is None and l2 is None:
                break
            elif l1 is None:
                l3.next = ListNode(l2.val)
                l2 = l2.next
            elif l2 is None:
                l3.next = ListNode(l1.val)
                l1 = l1.next

            else:
                if l1.val > l2.val:
                    l3 = ListNode(l2.val)
                    l2 = l2.next
                else:
                    l3 = ListNode(l1.val)
                    l1 = l1.next

            l3 = l3.next

        return l3Start
