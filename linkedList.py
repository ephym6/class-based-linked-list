class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None #points to first node

        def insert_at_end(self, data):
            new_node = Node(data)

            if self.head is None:
                self.head = new_node
                return

            last = self.head
            while last.next is not None:
                last = last.next

            last.next = new_node

        def insert_at_start(self, data):
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

        def insert_at_index(self, index, data):
            if index < 0 or index > len(self):
                raise ValueError("Index out of range")

            if index == 0:
                self.insert_at_start(data)
                return

            new_node = Node(data)
            curr_node = self.head
            position = 0

            while curr_node and position < index - 1:
                curr_node = curr_node.next
                position += 1

            if curr_node is None:
                raise ValueError("Index out of bounds")

            new_node.next = curr_node.next
            curr_node.next = new_node

            def delete_at_index(self, index):
                if self.head is None:
                    raise ValueError("List is empty")

                if index < 0 or index >= len(self):
                    raise ValueError("Index out of range")

                if index == 0:
                    self.head = self.head.next
                    return

                curr_node = self.head
                position = 0

                while curr_node and position < index - 1:
                    curr_node = curr_node.next
                    position += 1

                if curr_node is None or curr_node.next is None:
                    raise ValueError("Index out of bounds")

                curr_node.next = curr_node.next.next

            def search(self, value):
                curr_node = self.head
                index = 0

                while curr_node:
                    if curr_node.data == value:
                        return index
                    curr_node = curr_node.next
                    index += 1

                return -1

            def display(self):
                curr_node = self.head
                while curr_node:
                    print(curr_node.data, end=" -> ")
                    curr_node = curr_node.next

                print("None")