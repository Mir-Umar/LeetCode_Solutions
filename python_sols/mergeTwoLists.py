 # Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
         # Create a dummy node to start the merged list
        dummy = ListNode()
        current = dummy
        
        # Traverse both lists and compare the values of the nodes
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # Append the remaining nodes from either list if any
        if list1:
            current.next = list1
        else:
            current.next = list2
        
        return dummy.next
