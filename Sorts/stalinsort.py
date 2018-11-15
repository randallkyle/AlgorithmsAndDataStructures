from node import Node


class StalinSort:
    @staticmethod
    def sort(l):
        """Implement StalinSort"""
        # TODO Replace "pass" with your sort
        if l.next==None:
            return l
        
        while not l.next == None:
            ln = l.next
            
            if l.value > ln.value:
                l.next=ln.next
                ln.value=''


            #if ln.next.value!=None:
            else:
                l=l.next


                
            print(l.value,l.next)
       

            
            

if __name__ == '__main__':
    c=Node('2',None)
    b=Node('1',c)
    a=Node('3',b)
    print(a.next,b.next,c.next)
    StalinSort.sort(a)
    print(a.value,b.value,c.value)
    
