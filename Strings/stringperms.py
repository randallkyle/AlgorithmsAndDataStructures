def isUniqueChars(s):
    seenBefore=[]
    for i in range(len(s)):
        if s[i] in seenBefore:
            return False
        else:
            seenBefore.append(s[i])
    return True

def arePermutations(s ,t):

    for i in s:
        if i not in t:
            return False
    return True


#print(arePermutations("kyle", "elyk"))

def arePerms(s,t):
    countChars = [0] * 256
    for char in s:
        countChars[ord(char)] +=1

    countChars = [0] * 256
    for char in s:
        countChars[ord(char)] -=1

    return (countChars==[0]*256)

def isPermutationPalindrome(s):
    countChars = [0] * 256
    for char in s:
        countChars[ord(char)] +=1
    
    #only odd allowed
    odds=0
    for i in countChars:
        if i%2 != 0:
            odds+=1

    if odds > 1:
        return False
    else:
        return True





