from singly_linked_list import Node, LinkedList 

"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 
"""

# 1. Implement the Stack class using an array as the underlying storage structure. Make sure the Stack tests pass.
# class Stack:
#     def __init__(self, storage=None):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)

#     def push(self, value):
#         return self.storage.append(value)

#     def pop(self):
#         if len(self.storage) is not 0:
#             return self.storage.pop()
#         else:
#             return None

# 2. Re-implement the Stack class, this time using the linked list implementation as the underlying storage structure. Make sure the Stack tests pass.
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def pop(self):
        if self.size is not 0:
            self.size -= 1
            return self.storage.remove_tail()
        else:
            return None

# What is the difference between using an array vs. a linked list when implementing a Stack?
# Using Python lists enables us to use the method that come with it. However, for lists with unknown sizes, interacting with the values becomes very difficult if using arrays, so linked lists are better suited due to the nature of setting the head and tail. 