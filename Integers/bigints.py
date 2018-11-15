def addBigIntegers(a,b):
    prev=0
    place=1
    ac = a.head
    bc = b.head
    while(ac != None and bc != None):
        """ takes two linked lists of ints and adds them together """
        cc=(ac+bc+prev)//10
        dc+=((ac+bc)%10)*place
        ac = ac.next
        bc = bc.next
        place += 1

print(12//10, 12%10)
