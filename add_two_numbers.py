# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Extract number from l1
        l1_num = 0
        l1_power_count = 0
        while l1:
            l1_num += (l1.val * 10 ** l1_power_count)
            l1_power_count += 1
            l1 = l1.next
        
        # Extract number from l2
        l2_num = 0
        l2_power_count = 0
        while l2:
            l2_num += (l2.val * 10 ** l2_power_count)
            l2_power_count += 1
            l2 = l2.next

        # Sum numbers from l1 and l2
        final_sum = l1_num + l2_num

        if final_sum == 0:
            return ListNode(0)

        # Dummy node for appending
        dummy_head = ListNode()

        # Pointer for tracking
        current = dummy_head

        while final_sum > 0:
            # Retrieve correct digit
            temp_digit = final_sum % 10

            # Create node with correct digit
            temp_node = ListNode(temp_digit)

            # Append node at end
            current.next = temp_node

            # Move to next node
            current = current.next

            # Move one place value up along final sum
            final_sum //= 10
        
        return dummy_head.next
