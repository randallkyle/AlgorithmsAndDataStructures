
class binarySort:
    
    @staticmethod
    def sort(sortme):
        ''' Loop over the input list in N time, keeping track of largest and smallest values
        uses a logN time binary search function when a value must be inserted.

        '''
        if len(sortme)==1:
            return sortme
        
        sortedList=[]
        top = 0
        bottom = None
        
        for i in sortme:
            
            if not bottom and len(sortedList)>0:
                bottom=sortedList[0]
                
            if i >= top:
                sortedList.append(i)
                top=i
                print("add ", i)

            elif i<= bottom:
                sortedList.insert(0,i)
                bottom=i
                print("prepend ", i)

            else:
                print(sortedList)
                index = binarySort.binSort(sortedList,i,len(sortedList),0)
                sortedList.insert(index,i)
                print("insert ", i)

            #binary sort list
        return sortedList


    @staticmethod
    def binSort(data,value, high, low):
        ''' This is binary search with recursion and avoids changing the array
        '''
        m = int(((high-low)//2)+low)
        print("search ",m)
        if low >= high:
            return False
        if m-1 < 0:
            h=0
        else:
            h=m
        if value < data[m] and value >= data[h-1]:
            return m
        elif value < data[m]:
            return binarySort.binSort(data, value, m, low)
        else:
            return binarySort.binSort(data, value, high, m)
            



    
