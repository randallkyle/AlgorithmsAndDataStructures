#IT 310 Search Algorithms
import random
import time
import sys

class LinearSearch():
    """This class does a linear search on a list and resturns the first matching value. """

    def __init__(self):
        pass

    def search(self,data,value):
        counter = 0
        for i in data:
            if i == value:
                return counter
            else:
                counter += 1


class BinarySearch():
    """This class does a binary search over a set and returns the first matching value """

    def __init__(self):
        pass

    def searchR(self,data,value):
        
        if data[0]>=data[-1]:
            return False
        if value==data[h]:
            return value
        elif value < data[h]:
            return self.searchR(data[:h], value)
        elif value > data[h]:
            return self.searchR(data[h:], value)

    def searchRM(self,data,value, high, low):
        ''' This is binary search with recursion and avoids changing the array
        '''
        m = int(((high-low)/2)+low)
        if low>=high:
            return False
        if value==data[m]:
            return value
        elif value < data[m]:
            return self.searchRM(data, value, m, low)
        else:# value > data[m]:
            return self.searchRM(data, value, high, m)


    def search(self,data,value):
        counter = 0
        while True: # need to protect against infinite loops
            dl = len(data)
            i = int(dl/2)
            if data[i] == value:
                return counter
            else:
                if data[i] < value:
                    data = data[i:]
                else:
                    data = data[0:i+1]
            '''if counter > dl:
                print("error: infinite loop")
                break
            else:'''
            counter += 1


    def search1(self,data,value):
            counter = 0
            dl = len(data)
            i = int(dl/2)
            while data[i]!=value: # need to protect against infinite loops
                counter += 1
                if data[i] < value:
                    i += int(dl/((1+counter)**2))
                else:
                    i -= int(dl/((1+counter)**2))
                if i > dl-1:
                    i = dl-1
                elif i < 0:
                    i=0
                #print(i)
                #print(data[i],value)
            return counter
            

if __name__ == "__main__":
    sys.setrecursionlimit(1001)
    data=range(1,1000)
    print(data[0],data[-1])
    tries=1000

    millis = int(round(time.time() * 1000))
    counts = 0
    linear = LinearSearch()
    for i in range(0,tries):
        counts+=linear.search(data,random.randint(1,999))
    print("the average number for linear is: ", counts/tries)
    print(int(round(time.time() * 1000))-millis)
    
    counts = 0
    millis = int(round(time.time() * 1000))
    binary=BinarySearch()
    for i in range(0,tries):
        counts+=binary.searchRM(data,random.randint(1,999),999,1)
    print("the average number for binary is: ", counts/tries)
    print(int(round(time.time() * 1000))-millis)
    millis = int(round(time.time() * 1000))
    binary=BinarySearch()
    counts=0
    for i in range(0,tries):
        counts+=binary.searchR(data,random.randint(1,999))
    print("the average number for binary is: ", counts/tries)
    print(int(round(time.time() * 1000))-millis)

