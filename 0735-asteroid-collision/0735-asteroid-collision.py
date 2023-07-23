class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []
        for a in asteroids:
            while(s and a<0<s[-1]):
                if(abs(a)>s[-1]):
                    s.pop()
                elif(abs(a)==s[-1]):
                    s.pop()
                    break
                else:
                    break
            else:
                s.append(a)
        return s