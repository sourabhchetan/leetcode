# Definition for singly-linked list node.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        curr = head

        while curr:
            # Check if current value has duplicates
            if curr.next and curr.val == curr.next.val:
                duplicate = curr.val

                # Skip all nodes with this value
                while curr and curr.val == duplicate:
                    curr = curr.next

                prev.next = curr
            else:
                prev = curr
                curr = curr.next

        return dummy.next