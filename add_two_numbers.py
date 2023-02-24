from typing import Optional
from custom_realisations.node import ListNode

"""
    You are given two non-empty linked lists representing two non-negative integers.
    The digits are stored in reverse order, and each of their nodes contains a single digit.
    Add the two numbers and return the sum as a linked list.
    You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""


def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    result = ListNode()
    first = result
    while l1 or l2:
        if not l1:
            l1 = ListNode()
        elif not l2:
            l2 = ListNode()
        result.val += l1.val + l2.val
        if result.val >= 10:
            result.next = ListNode()
            result.next.val += result.val // 10
            result.val = result.val % 10

        l1 = l1.next
        l2 = l2.next
        if (l2 or l1) and not result.next:
            result.next = ListNode()
        result = result.next
    return first


def add_two_numbers_memory_runtime(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    head = ListNode(0)
    cur = head
    res = 0
    while l1 or l2 or res > 0:
        num1 = l1.val if l1 else 0

        num2 = l2.val if l2 else 0
        res, val = divmod(num1 + num2 + res, 10)
        cur.next = ListNode(val)
        cur = cur.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return head.next


n1 = ListNode(2)
n1.next = ListNode(4)
n1.next.next = ListNode(3)

n2 = ListNode(5)
n2.next = ListNode(6)
n2.next.next = ListNode(4)

res = add_two_numbers(n1, n2)
while res is not None:
    print(res.val)
    res = res.next
