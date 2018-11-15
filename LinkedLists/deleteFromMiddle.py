def deleteFromMiddle(node):
    ''' deletes the node from the list'''
    node.value=node.next.value #changes the value to the next node's value
    node.next=node.next.next   #changes the pointer to point at the value after the next node

'''
a -> b -> c -> d ->

a -> c -> c -> d ->

a -> c      -> d ->

'''

