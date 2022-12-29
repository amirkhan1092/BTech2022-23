'''
• 2. Add Two Numbers
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]'''
from typing import List, Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 1. create a dummy node
        dummy = ListNode(0)
        # 2. create a pointer to the dummy node
        p = dummy
        # 3. create a carry variable
        carry = 0
        # 4. loop through the linked list
        while l1 or l2:
            # 5. check if l1 is not None
            if l1:
                # 6. add the value of l1 to the carry
                carry += l1.val
                # 7. move l1 to the next node
                l1 = l1.next
            # 8. check if l2 is not None
            if l2:
                # 9. add the value of l2 to the carry
                carry += l2.val
                # 10. move l2 to the next node
                l2 = l2.next
            # 11. create a new node with the value of the carry
            p.next = ListNode(carry % 10)
            # 12. move p to the next node
            p = p.next
            # 13. update the carry
            carry = carry // 10
        # 14. check if carry is greater than 0
        if carry > 0:
            # 15. create a new node with the value of the carry
            p.next = ListNode(carry)
        # 16. return the dummy node
        return dummy.next

# Path: leetcode problems\addTwoNumber.py
# main code
if __name__ == '__main__':
    # 1. create a linked list
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    # 2. create an object of the class
    obj = Solution()
    # 3. call the method
    print(obj.addTwoNumbers(l1, l2))    
    