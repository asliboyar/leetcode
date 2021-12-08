class Solution:
    def fib(self, n: int) -> int:
        if n >  1:
            point1 = 0
            point2 = 1
            for i in range(2,n+1):
                a = point2
                point2 = point1 + point2
                point1 = a 
            return point2
        else:
            return n
