class Solution:
    def decodeString(self, s: str) -> str:
        x=[]
        z=""
        c=0
        for i in s:
            if(i=="["):
                x.append(z)
                x.append(c)
                z=""
                c=0
            elif(i=="]"):
                num=x.pop()
                prev=x.pop()
                z=prev+num*z
            elif(i.isdigit()):
                c=c*10+int(i)
            else:
                z+=i
        return z



        