# https://www.hackerrank.com/challenges/30-linked-list/problem

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert(self, head, data):
        node = Node(data)
        if head is None:
            head = node
            return head
        tail = head
        while tail.next is not None:
            tail = tail.next
        tail.next = node
        return head
