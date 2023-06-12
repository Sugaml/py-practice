# Defining the Node class for linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

# Creating a linked list
node1=Node(1)
node2=Node(2)
node3=Node(3)

node1.next=node1
node2.next=node3

#Accessing elements by traversing the linked list
current_node=node1
while current_node is not None:
    print(current_node.data)
    current_node=current_node.next