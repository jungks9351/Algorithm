class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # solution1
        return any(target in row for row in matrix)
        # matrix[row][column] == target => True
        # 아니면 False
        # matrix 가 존재하지않으면 False

        
        # # solution2
        # # 예외 처리
        # if not matrix:
        #     return False
        #
        # # 첫 행의 맨 뒤
        # row = 0
        # col = len(matrix[0]) - 1
        #
        # while row <= len(matrix) - 1 and col >= 0:
        #     if target == matrix[row][col]:
        #         return True
        #     # 타겟이 작으면 왼쪽으로
        #     elif target < matrix[row][col]:
        #         col -= 1
        #     # 타겟이 크면 아래로
        #     elif target > matrix[row][col]:
        #         row += 1
        # return False
        #
        # # solution3
        # mLen = len(matrix)
        # if mLen == 0:
        #     return False
        #
        # row = 0
        #
        # while row < mLen:
        #     column = 0
        #     while column < len(matrix[0]) - 1 and matrix[row][column]<target:
        #         column += 1
        #     if matrix[row][column] == target:
        #         return True
        #     row += 1
        # return False
        #
        # # soultion4
        # for i in range(len(matrix)):
        #     # print(i)
        #     for j in range(len(matrix[0])):
        #         # print(j)
        #         if matrix[i][j] == target:
        #             return True
        #
        # return False









