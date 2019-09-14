https://www.hackerrank.com/challenges/find-the-merge-point-of-two-joined-linked-lists/problem
Find Merge Point of Two Lists

# Complete the findMergeNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def findMergeNode(head1, head2):

    while head1 != None:
        temp2 = head2

        while temp2 != None:
            if temp2 == head1:
                return temp2.data

            temp2 = temp2.next

        head1 = head1.next

    return head1.data
