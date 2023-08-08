class Solution:
    def countPrimes(self, n: int) -> int:
        c=0
        p=[]
        for i in range(n+1):
            p.append(True)
        i=2
        while(i*i<n):
            if(p[i]==True):
                for j in range(i*i,n+1,i):
                    p[j]=False
            i+=1
        for k in range(2,n):
            if(p[k]==True):
                c+=1
        return c




