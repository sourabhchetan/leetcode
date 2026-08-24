class Solution(object):
    def partition(self, head, x):
        # Dummy nodes for the two partitions
        less_dummy = ListNode(0)
        greater_dummy = ListNode(0)

        less = less_dummy
        greater = greater_dummy

        while head:
            if head.val < x:
                less.next = head
                less = less.next
            else:
                greater.next = head
                greater = greater.next

            head = head.next

        # Connect the two partitions
        less.next = greater_dummy.next

        # Important: terminate the list
        greater.next = None

        return less_dummy.next
