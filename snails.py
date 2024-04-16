
def snails(matrix):
    res = []
    if len(matrix) == 0:
        return res
    row_begin = 0
    row_end = len(matrix) - 1
    col_begin = 0
    col_end = len(matrix[0]) - 1

    while row_begin <= row_end and col_begin <= col_end:
        for i in range(col_begin, col_end+1):
            res.append(matrix[row_begin][i])
        row_begin += 1

        for i in range(row_begin, row_end+1):
            res.append(matrix[i][col_end])
        col_end -= 1

        if row_begin <= row_end:
            for i in range(col_end, col_begin-1, -1):
                res.append(matrix[row_end][i])
        row_end -= 1

        if col_begin <= col_end:
            for i in range(row_end, row_begin-1, -1):
                res.append(matrix[i][col_begin])
        col_begin += 1

    return res

matrix = []
rows = int(input("enter number of rows of matrix: "))
columns = int(input("enter number of columns of matrix: "))
for i in range(rows):
    empty_list=[]
    for j in range(columns):
        print(f"enter {i}{j} element:")
        empty_list.append(int(input()))
    matrix.append(empty_list)

result = snails(matrix)
print(f"the result is : {result}")