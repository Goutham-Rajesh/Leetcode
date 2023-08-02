class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        d1={}
        l1=[]
        l2=[]
        for i in word1:
            if i not in d1:
                d1[i]=1
            else:
                d1[i]+=1
        d2={}
        for i in word2:
            if i not in d2:
                d2[i]=1
            else:
                d2[i]+=1
        
        for i in d1.values():
            l1.append(i)
        for i in d2.values():
            l2.append(i)
        print(l1)
        print(l2)
        l1.sort()
        l2.sort()
        if(l1==l2):
            for i in word1:
                if i not in word2:
                    return False
            return True
        
        