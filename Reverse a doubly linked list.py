https://www.hackerrank.com/challenges/reverse-a-doubly-linked-list/problem
Reverse a doubly linked list

# Complete the reverse function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def reverse(head):

    temp = None
    curr = head

    while curr != None:
        temp = curr.prev
        curr.prev = curr.next
        curr.next = temp

        curr = curr.prev

    if temp != None:
        head = temp.prev

    return head
 
