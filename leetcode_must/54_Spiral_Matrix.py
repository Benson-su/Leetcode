iclass Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        dirr = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        m = len(matrix)
        n = len(matrix[0])
        matrix_num = m * n
        output = []
        visited = [[0] * n for i in range(m)]
        dir_pointer = 0
        orix, oriy = 0, 0
        output.append(matrix[0][0])
        visited[0][0] = 1
        while len(output) < matrix_num:
            x, y = dirr[dir_pointer%4]
            orix += x
            oriy += y
            if  m > orix >= 0 and n > oriy >= 0 and not visited[orix][oriy]:     
                output.append(matrix[orix][oriy])
                visited[orix][oriy] = 1
            else:
                orix -= x
                oriy -= y
                dir_pointer += 1
        return output
            
        
