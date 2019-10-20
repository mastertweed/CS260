# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):

        head = ListNode(0)
        a = head

        carry = 0
        while True:
            num = l1.val + l2.val + carry
            if num >= 10:
                a.val = num - 10
                carry = 1
            else:
                a.val = num
                carry = 0

            if l1.next == None and l2.next == None:
                if carry == 1:
                    a.next = ListNode(1)
                else:
                    return head

            if l1.next == None:
                l1.next = ListNode(0)
            if l2.next == None:
                l2.next = ListNode(0)

            l1 = l1.next
            l2 = l2.next
            a.next = ListNode(0)
            a = a.next