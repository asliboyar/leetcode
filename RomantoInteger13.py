class Solution:
    def romanToInt(self, s: str) -> int:
        a = {"I": 1, "V": 5, "X":10, "L": 50, "C": 100, "D": 500, "M":1000}
        n = len(s)
        b = n-1
        count = 0 
        while b>=0:
            if b<n-1 and a[s[b]]<a[s[b+1]]:
                count-=a[s[b]]
            else:    
                count+=a[s[b]]
            b-=1
        return  count
