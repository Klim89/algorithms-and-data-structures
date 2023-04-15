class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


head = Node(1, Node(2, Node(3, Node(4))))


def insert_start(self, data):
    new_node = Node(data)
    new_node.next = self.start_node
    self.start_node = new_node


def print_list(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()


print_list(head)


def reverse_list(head, tail=None):
    while head:
        head.next, tail, head = tail, head, head.next
    return tail


print_list(reverse_list(head))
