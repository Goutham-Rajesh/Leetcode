class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate=list(senate)
        x=[]
        y=[]
        n=len(senate)
        for i in range(len(senate)):
            if(senate[i]=="R"):
                x.append(i)
            else:
                y.append(i)
        while(x and y):
            if(x[0]<y[0]):
                y.pop(0)
                x.pop(0)
                x.append(n)
                n+=1
            else:
                y.pop(0)
                x.pop(0)
                y.append(n)
                n+=1
        if(y):
            return "Dire"
        else:
            return "Radiant"


            
        
        