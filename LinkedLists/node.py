class Node:
    """Simple node for singly-linked list"""

    def __init__(self, value, next=None):
        """Create a new node, with optional next node pointer"""
        self.value = value
        self.next = next

    def __str__(self):
        return self.value
