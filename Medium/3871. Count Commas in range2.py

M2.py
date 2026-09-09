class Solution(object):
    def countCommas(self, n):
        total = 0
        
        # Numbers starting from 1000 have at least 1 comma
        start = 1000
        commas = 1
        
        while start <= n:
            # Numbers from start to start*1000 - 1
            end = start * 1000 - 1
            
            count = min(n, end) - start + 1
            
            if count > 0:
                total += count * commas
            
            start *= 1000
            commas += 1
        
        return total