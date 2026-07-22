class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or not head.next or k == 0:
            return head

        # Find length and last node
        length = 1
        tail = head

        while tail.next:
            tail = tail.next
            length += 1

        # Avoid unnecessary rotations
        k %= length

        if k == 0:
            return head

        # Make the list circular
        tail.next = head

        # New tail is at position length - k - 1
        steps = length - k
        new_tail = tail

        while steps:
            new_tail = new_tail.next
            steps -= 1

        # Break the circle
        new_head = new_tail.next
        new_tail.next = None

        return new_head