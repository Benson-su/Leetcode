# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        tmp_node = ListNode(0)
        tmp_node.next = head
        num = 0
        while head:
            num += 1
            head = head.next
        if num == 1 and n > 0:
            return None
        head = tmp_node.next
        counter = 0
        
        if num == n:
            tmp_node.next = tmp_node.next.next
            return tmp_node.next
            
        while head:
            counter += 1
            if counter == num - n:
                head.next = head.next.next
            else:
                head = head.next
        return tmp_node.next
        
        
