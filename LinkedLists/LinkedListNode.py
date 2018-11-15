class LinkedListNode:
    """Single node for singly linked list"""
    
    def __init__(self,element=None,_next=None):
        self.element=element
        self._next=_next

    def __str__(self):
        return str(self.element)

    def get_element(self):
        return self.element

    def get_next(self):
        return self._next
    
    def set_next(self,next_node):
        self._next=next_node

    def set_element(self,new_element):
        self.element=new_element



    

    
        
