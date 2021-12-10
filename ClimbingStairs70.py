class Solution:
    def climbStairs(self, n: int) -> int:
        p1 = 1
        p2 = 1
        for i in range(n):
            a = p2
            p2=p1+p2
            p1=a
        return p1
