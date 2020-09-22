# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head == None or head.next == None:
            return head
        temp = head
        length = 1
        while temp.next != None:        
            temp = temp.next
            length += 1
        k %= length
        if k==0:
            return head
        for i in range(k):
            temp = head
            while True:
                if temp.next == None:
                    tail.next = None
                    temp.next = head
                    head = temp
                    break
                tail = temp
                temp = temp.next
        return head