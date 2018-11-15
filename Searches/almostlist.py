class AlmostList:
    '''A list-like structure that can only hold positive integers and only supports elementAt()'''

    def __init__(self, array):
        self.data = array

    def __getitem__(self, i):
        '''Return element at index, or None if index is past end of array'''
        if i < len(self.data):
            return self.data[i]
        else:
            return None

    def __len__(self):
        return 0


