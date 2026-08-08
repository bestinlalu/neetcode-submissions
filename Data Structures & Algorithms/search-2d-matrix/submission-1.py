class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix)
        l = 0
        r = m - 1
        x = -1
        while(l <= r):
            mid = (l + r) // 2
            if((mid != m - 1 and matrix[mid][0] < target and 
                matrix[mid + 1][0] > target) or
                (mid == m - 1 and matrix[mid][0] < target)):
               x = mid
               break
            elif(matrix[mid][0] == target):
                return True
            elif(matrix[mid][0] < target):
                l = mid + 1
            else:
                r = mid - 1
        if(x == -1):
            return False
        n = len(matrix[0])
        l = 0
        r = n - 1
        while(l <= r):
            mid = (l + r) // 2
            if(matrix[x][mid] < target):
               l = mid + 1
            elif(matrix[x][mid] > target):
                r = mid - 1
            else:
                return True
        return False