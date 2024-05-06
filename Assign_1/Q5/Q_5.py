def matrix_multiply(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        return "Error: The number of columns in the first matrix must be equal to the number of rows in the second matrix."
    result = [[sum(x*y for x, y in zip(matrix1_row, matrix2_col)) for matrix2_col in zip(*matrix2)] for matrix1_row in matrix1]
    return result

def main():
    matrix1 = [[1, 2, 3], [4, 5, 6]]
    matrix2 = [[7, 8], [9, 10], [11, 12]]
    print(matrix_multiply(matrix1, matrix2))

if __name__ == "__main__":
    main()
