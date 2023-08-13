
class Solution:
    def nthFibonacci(self, n : int) -> int:
        # code here
        m=1000000007
        f=0
        s=[0]*(n+1)
        s[1]=1
        for i in range(2,n+1):
            s[i]=(s[i-1]+s[i-2])%m
            
        return s[n]
            
        


#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        obj = Solution()
        res = obj.nthFibonacci(n)
        
        print(res)
        

# } Driver Code Ends