# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], carry=0) -> Optional[ListNode]:
        # 这个题是按从小到大排列的，如果是从大到小排列尼？那就先把两个链表进行翻转，再进行下面的处理
        if not l1 and not l2 and carry == 0:
            return None
        
        s = carry
        if l1:
            s += l1.val
            l1 = l1.next
        if l2:
            s += l2.val
            l2 = l2.next
        
        return ListNode(s % 10, self.addTwoNumbers(l1, l2, s // 10))
        