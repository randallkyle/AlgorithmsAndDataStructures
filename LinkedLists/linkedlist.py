from node import Node


class LinkedList:

    '''implement the linked list class?'''
    
    @staticmethod
    def sort(l):
        """Simple in-place sort of singly-linked list whose head is l"""
        # TODO Replace "pass" with your sort
        if l.next==None:
            return l
        
        while not l.next == None:
            ln = l.next
            while not ln == None:
                if l.value > ln.value: #swap the two
                    temp = l.value
                    l.value = ln.value
                    ln.value = temp
                ln=ln.next
            l=l.next
       

            
            

if __name__ == '__main__':
    c=Node('that',None)
    b=Node('this',c)
    a=Node('thet',b)
    print(a,b,c)
    LinkedList.sort(a)
    print(a,b,c)
    
#C - understand basics
#B - C and details
#A - B and fix code
