def RotateClockwise(matrix):
    # TODO
    #  [
    #    [1,2,3],
    #    [4,5,6],
    #    [7,8,9],
    #  ]
    #  [
    #    [7,4,1],
    #    [8,5,2],
    #    [9,6,3],
    #  ]
    matrixLength = len(matrix)
    
    for row in range(matrixLength):
        for col in range(row+1, matrixLength):
            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
    
    for row in matrix:
        row.reverse()
    
    return matrix

def RotateAntiClockwise(matrix):
    # TODO
    #  [
    #    [1,2,3],
    #    [4,5,6],
    #    [7,8,9],
    #  ]
    #  [
    #    [7,4,1],
    #    [8,5,2],
    #    [9,6,3],
    #  ]
    matrixLength = len(matrix)
    
    for row in range(matrixLength):
        for col in range(row+1, matrixLength):
            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
    
    for col in range(matrixLength):
        top, bottom = 0, matrixLength-1
        while top<bottom:
            matrix[top][col], matrix[bottom][col] = matrix[bottom][col], matrix[top][col]
            top+=1
            bottom-=1
    
    return matrix

inputMatrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]
print("Input Matrix:")
print(inputMatrix)
print("Clockwise Rotation:")
print(RotateClockwise(inputMatrix))
print("Anti-Clockwise Rotation:")
print(RotateAntiClockwise(inputMatrix))
print(RotateAntiClockwise(inputMatrix))