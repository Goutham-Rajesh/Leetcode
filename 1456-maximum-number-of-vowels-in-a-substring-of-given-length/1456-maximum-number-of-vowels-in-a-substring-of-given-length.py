class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        v="aeiou"
        c=0
        m=c
        for i,j in enumerate(s) :
            if(j in v):
                c+=1
            if(s[i-k] in v and i>=k):
                c-=1
            m=max(m,c)
        return m
            
        
            
        