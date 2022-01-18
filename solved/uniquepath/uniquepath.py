class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        moves = m + n - 2
        low = min(m-1, n-1)
        r = min(moves - low, low)
        divided = 1
        divider = 1
        for i in range(r) : 
            divided *= moves - i
            divider *= i + 1
        return divided // divider
        