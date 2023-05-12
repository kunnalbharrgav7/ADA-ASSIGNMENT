# Implement a divide-and-conquer algorithm for sorting a linked list.


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge(left, right):
    if not left:
        return right
    if not right:
        return left

    if left.val < right.val:
        left.next = merge(left.next, right)
        return left
    else:
        right.next = merge(left, right.next)
        return right

def split(head):
    if not head:
        return None, None

    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    right = slow.next
    slow.next = None
    return head, right

def merge_sort(head):
    if not head or not head.next:
        return head

    left, right = split(head)
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)
