
def reverse(palindrome):
    prev=None
    current=palindrome.head
    while(current != None):
        nextnode = current.next
        current.next = prev
        prev = current
        current = nextnode

    return current

def isPalindrome(palindrome):
    """takes a list and tells if its a palindrome.

    """
    rev=reverse(palindrome)
    current=palindrome.head
    currentR=rev.head
    while(current != None and currentR != None):
        if current != currentR:
            return False
    
        currentR= currentR.next
        current = current.next     

    return (current == None and currentR == None)



