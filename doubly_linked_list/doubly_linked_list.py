"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        self.length += 1

        if self.head is None:
            new_head = ListNode(value)
            self.head = new_head
            self.tail = self.head
        else:
            new_head = ListNode(value)
            old_head = self.head
            new_head.next = old_head
            old_head.prev = new_head
            self.head = new_head
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        self.length -= 1
        value = self.head.value
        
        if self.head is self.tail:
            self.head = self.tail = None
            return value
        else:
            self.head = self.head.next
            self.head.prev = None
            return value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        self.length += 1

        if self.tail is None:
            new_tail = ListNode(value)
            self.tail = new_tail
            self.head = self.tail
        else:
            new_tail = ListNode(value)
            old_tail = self.tail
            new_tail.prev = old_tail
            old_tail.next = new_tail
            self.tail = new_tail
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        self.length -= 1
        value = self.tail.value
        
        if self.head is self.tail:
            self.head = self.tail = None
            return value
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            return value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if node is self.tail:
            self.tail = node.prev
            self.tail.next = None
            node.prev = None
            node.next = self.head
            self.head.prev = node
            self.head = node
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.prev = None
            node.next = self.head
            self.head.prev = node
            self.head = node
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if node is self.head:
            self.head = node.next
            self.head.prev = None
            node.next = None
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.next = None
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        self.length -= 1

        if node.next is None and node.prev is None:
            self.head = self.tail = None
        elif node is self.head:
            self.head.next.prev = None
            self.head = self.head.next
        elif node is self.tail:
            self.tail = self.tail.prev
            self.tail.prev.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if not self.head:
            return None
        
        max_value = self.head.value
        current = self.head.next

        while current:
            if current.value > max_value:
                max_value = current.value
            
            current = current.next

        return max_value