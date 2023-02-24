from custom_realisations.node import ListNode

"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""


def merge_two_lists(list1: ListNode = None, list2: ListNode = None) -> ListNode | None:
    cur = dummy = ListNode()
    while list1 and list2:
        if list1.val < list2.val:
            cur.next = list1
            list1, cur = list1.next, list1
        else:
            cur.next = list2
            list2, cur = list2.next, list2

    if list1 or list2:
        cur.next = list1 if list1 else list2

    return dummy.next


n1 = ListNode(1)
n1.next = ListNode(2)
n1.next.next = ListNode(4)

n2 = ListNode(1)
n2.next = ListNode(3)
n2.next.next = ListNode(5)

res = merge_two_lists(n1, n2)
while res is not None:
    print(res.val)
    res = res.next
