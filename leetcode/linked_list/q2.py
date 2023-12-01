from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        # Move the slow pointer one step and the fast pointer two steps at a time through the linked list,
        # until they either meet or the fast pointer reaches the end of the list.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                # If the pointers meet, there is a cycle in the linked list.
                # Reset the slow pointer to the head of the linked list, and move both pointers one step at a time
                # until they meet again. The node where they meet is the starting point of the cycle.
                slow = head
                while slow != fast:
                    # 確実にもう一度衝突する
                    print(slow.val)
                    print(fast.val)
                    slow = slow.next
                    fast = fast.next
                return slow

        # If the fast pointer reaches the end of the list without meeting the slow pointer,
        # there is no cycle in the linked list. Return None.
        return None

node0 = ListNode(3)
node1 = ListNode(2)
node2 = ListNode(0)
node3 = ListNode(-4)

node0.next = node1
node1.next = node2
node2.next = node3
node3.next = node1

print(Solution().detectCycle(node0).val)
