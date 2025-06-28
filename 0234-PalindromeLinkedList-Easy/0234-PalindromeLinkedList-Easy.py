# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        middle = self.middleNode(head)
        new = self.reverseLinkedList(middle)
        while new:
            if new.val != head.val:
                return False
            new = new.next
            head = head.next
        return True
    
    # 206. 反转链表
    def reverseLinkedList(self, head):
        pre, cur = None, head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre
            
    # 876. 链表的中间结点
    def middleNode(self, head):
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
        