# leetcode question link : https://leetcode.com/problems/find-the-winner-of-the-circular-game/

def findTheWinner(self, n: int, k: int) -> int:
    q=[]        
    for x in range(1, n+1):
        q.append(x)
    while(len(q) > 1):    
        l = k-1
        while l > 0 :
            temp = q[0]                
            q.pop(0)   
            q.append(temp)                   
            l = l-1
            q.pop(0)
    return q[0]

