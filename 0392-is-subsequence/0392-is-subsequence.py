class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sl=0
        i=0
        e=""
        while(sl<len(t) and i<len(s)):
            if(s[i]==t[sl]):
                e+=t[sl]
                i+=1
            sl+=1
        if(e==s):
            return True