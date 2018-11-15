import unittest
from almostlist import AlmostList
from os import sys

class AlmostSearch:
    @staticmethod
    def search(almostList, value, i=0):
        '''Search sorted AlmostList for value and return its index, or None if not there'''
        comp = almostList[i]
        if comp == None and i == 0:
            return None
        if comp == None or comp > value:
            # passed the value, so it is in between i and i/2
            return AlmostSearch.binSearch(almostList, value, i, i//2)
            
        elif comp == value:
            return i

        else:# almostList[i] < value:
            # increase the list index by double
            if i==0: # two times zero is still zero, avoid this by incrementing by one
                i+=1
            else:
                i=i*2
            return AlmostSearch.search(almostList, value, i)



    @staticmethod
    def binSearch(data, value, high, low):
        ''' This is binary search with recursion and avoids changing the array
        '''
        #create the midpoint
        m = int(((high-low)//2)+low)
        val=data[m]
        
        if val==None:
            # if the value is still past the end of the array
            return AlmostSearch.binSearch(data, value, m-1, low)
        if low > high:
            # if the value is not in the array
            return None
        elif value==val:
            # we found a match
            return m
        elif value < val:
            # choose the lower half of array
            return AlmostSearch.binSearch(data, value, m-1, low)
        else:
            # choose the upper half of the array
            return AlmostSearch.binSearch(data, value, high, m+1)

 
if __name__ == "__main__":
    print(AlmostSearch.search(AlmostList([-22, -11, 0, 11, 22, 33, 44, 55, 66, 77, 88, 99]), 44) == 4)
    print(AlmostSearch.search(AlmostList([-22, -11, 0, 11, 22, 33, 44, 55, 66, 77, 88, 99]), -22) == 0)
    print(AlmostSearch.search(AlmostList([-66, -55, -44, -33, -22, -11, 0, 11, 22, 33, 44, 55, 66, 77, 88, 99, 88]), 88) == None)


