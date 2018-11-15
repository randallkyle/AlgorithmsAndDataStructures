import math
class StringEdit:
    @staticmethod
    def off_by_one(s, t):
        '''Returns true if s and t differ by at most one edit'''
        # TODO Add code here (and any required helper methods below it)
        #insert, delete, replace
        error=0
        if s == t:
            return True # ????
        
        #if they are more than one character longer/shorter
        if abs(len(t)-len(s))>1:
            return False

        
        #if one is longer than other check for insert or delete
        #delete and insert are funcitonally the same
        if len(t)!=len(s):
            if len(t)<len(s):
                a=s
                s=t
                t=a

            #if len(t)-len(s)=1
            for i in range(len(s)):
                if s[i]!=t[i] and s[i]==t[i+1]: #if a delete needed
                    t=t[:i]+t[i+1:]
                    #print(t)
                    #print(s)
                    error+=1
                
            if error==0: # if the error is at the end
                error+=1

        
        #if same length: find error and replace to make the same
        if len(s)==len(t):
            for i in range(len(t)):
                if s[i]==t[i]:
                    pass
                else:
                    if(error==1):
                        return False
                    
                    error+=1
                    s=s[:i]+t[i]+s[i+1:]
                    #print(s,t)
      

        
        if error>1:
            return False
        # check to see if a string is off
        
        #if the strings are the same return true
        if s==t:
            return True
        
        
        return True


    
stringedit=StringEdit()
print(stringedit.off_by_one("aaa","aba"))#T
print(stringedit.off_by_one("aaa","aaab"))#f
print(stringedit.off_by_one("aaa","aa"))#T



