class Solution:    
    def findUnion(self, a, b):
        # code here
        n = a+b
        r = len(set(n))
        return r