class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1={}
        d2={}
        for i in s:
            if i not in d1:
                d1[i]=1
            else:
                d1[i]+=1
        for j in t:
            if j not in d2:
                d2[j]=1
            else:
                d2[j]+=1
        print(d1)
        print(d2)
        if(d1==d2):
            return True
        else:
            return False