from linkedlistqueue import LinkedListQueue


class BigInteger:
    @staticmethod
    def add(a, b):
        """Add two integers represented as LinkedListQueues, least-significant-digit first"""
        result = LinkedListQueue()
        remainder=0
        # TODO Add code here
        if len(a)>len(b):
            c=a
            a=b
            b=c
            
        #loop through the longer queue
        while b.is_empty()!=True:

            #no more addition for ac if it is empty
            if a.is_empty():
                ac=0
            else:
                ac=a.dequeue()

            bc=b.dequeue()
            cc=ac+bc+remainder

            if cc>9:
                remainder=1
                cc-=10
            else:
                remainder=0

            result.enqueue(cc)
            
        if remainder==1:
            result.enqueue(1)
            
        return result


def simpleTest():
    # You do not have to include this method in your submission, but it or
    # methods like it will help you while debugging your code.
    # For example, here's the code to replicate the example:
    a = LinkedListQueue()  # will hold 6 1 7
    a.enqueue(7)
    b = LinkedListQueue()  # will hold 2 9 5
    b.enqueue(9)
    b.enqueue(9)
    c = BigInteger.add(a, b)  # should now hold 9 1 2
    print(c.dequeue())  # should print 2
    print(c.dequeue())  # should print 1
    print(c.dequeue())
    print(len(c))  # should print 0 (nothing left in list)

#  617 + 295 = 912 as (7->1->6) + (5->9->2) = (2->1->9)
print(simpleTest())
