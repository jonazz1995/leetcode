# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
       
def recursion(head):
    if not head:
        return None
    newHead = head
    if head.next:
        newHead = recursion(head.next)
        head.next.next = head
    head.next = None
    return newHead

node1 = ListNode(1)
node2 = ListNode(2)
node1.next = node2

print(recursion(node1).val)
