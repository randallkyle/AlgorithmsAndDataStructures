def printKthToLast(head, k)
    '''    '''
    current=head.head           # set to head
    counter=1                   # counter set to first node
    
    length=1
    while current.next:
        lenght+=1
        current=current.next
    kth=length-k

    current=current.head
    while counter!=kth:         # while the counter hasn't reached the Kth node
        current=current.next    # update the current node to the next node
        counter+=1              # update the counter
    print(current.value)        # print the next value since we are on the Kth node

    
    



def recursiveHelper(node,k):
    ''' returns the pointer of the Kth element after node'''
    if k==1:                               # if this element is the kth node 
        return node.next                   # return the node's pointer (null if at end)
    return recursiveHelper(node.next,k-1)  # decrement k and move to next node

def printKthToLastR(head,k):
    if !recursiveHelper(head,k):           # if the kth element from current node is null
        return head.value                  # you are sitting on the kth element from the end, print the value!
    return printKthToLastR(head.next,k)    # move the current element to the next element
    


'''
a->b->c->d->e->f

'''
