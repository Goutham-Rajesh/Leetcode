class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        c=0
        d={}
        for i in grid:
            if(str(i) not in d):
                d[str(i)]=1
            else:
                d[str(i)]+=1
        for i in range(len(grid)):
            l=[]
            for j in range(len(grid)):
                l.append(grid[j][i])
            if(str(l) in d):
                c+=d[str(l)]
            
        return c