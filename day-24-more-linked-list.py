# https://www.hackerrank.com/challenges/30-linked-list-deletion/problem

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Solution:
    def insert(self,head,data):
            p = Node(data)
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def removeDuplicates(self, head):
        val_nodes = []
        current_node = head
        while current_node:
            if not current_node.data in val_nodes:
                val_nodes.append(current_node.data)
            current_node = current_node.next

        if len(val_nodes) > 0:
            head = Node(val_nodes[0])
            for i in range(1, len(val_nodes)):
                self.insert(head, val_nodes[i])

        return head
