class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        low, high = 0, (row * col) - 1
        while low <= high:
            mid = low + (high - low) // 2
            curr = matrix[mid // col][mid % col]
            if curr == target: return True
            elif curr > target: high = mid - 1
            else: low = mid + 1
        return False