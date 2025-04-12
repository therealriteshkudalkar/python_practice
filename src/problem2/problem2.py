from typing import Optional


class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt

    def __repr__(self):
        return f"<Node(val={self.val}, next={self.next}>"

class Solution:

    @staticmethod
    def swap_pairs(head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        elif head.next is None:
            return head
        else:
            # At least two nodes are present
            temp_1 = head
            temp_2 = head.next
            new_head = temp_2
            current_head = None
            while temp_1 is not None and temp_2 is not None:
                temp_1.next = temp_2.next
                temp_2.next = temp_1

                if current_head is None:
                    current_head = temp_1
                else:
                    current_head.next = temp_2
                    current_head = temp_1

                temp_1 = temp_1.next
                temp_2 = None if temp_1 is None else temp_1.next

            return new_head
