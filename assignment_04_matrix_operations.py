# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
def read_matrix(rows, columns):
    matrix = []

    for i in range(rows):
        row = list(map(int, input(f"Enter row {i + 1}: ").split()))

        while len(row) != columns:
            print(f"Please enter exactly {columns} values.")
            row = list(map(int, input(f"Enter row {i + 1}: ").split()))

        matrix.append(row)

    return matrix


def display_matrix(matrix):
    for row in matrix:
        for value in row:
            print(f"{value:6}", end="")
        print()


def transpose_matrix(matrix):
    transposed = []

    for column in range(len(matrix[0])):
        new_row = []

        for row in range(len(matrix)):
            new_row.append(matrix[row][column])

        transposed.append(new_row)

    return transposed


def add_matrices(matrix_a, matrix_b):
    result = []

    for row in range(len(matrix_a)):
        new_row = []

        for column in range(len(matrix_a[0])):
            value = matrix_a[row][column] + matrix_b[row][column]
            new_row.append(value)

        result.append(new_row)

    return result


def multiply_matrices(matrix_a, matrix_b):
    result = []

    for row in range(len(matrix_a)):
        new_row = []

        for column in range(len(matrix_b[0])):
            total = 0

            for i in range(len(matrix_b)):
                total = total + matrix_a[row][i] * matrix_b[i][column]

            new_row.append(total)

        result.append(new_row)

    return result


def main():
    print("Matrix Operations")
    print("1. Transpose a matrix")
    print("2. Add two matrices")
    print("3. Multiply two matrices")
    choice = input("Choose an operation (1-3): ")

    if choice == "1":
        rows = int(input("Enter number of rows: "))
        columns = int(input("Enter number of columns: "))
        matrix = read_matrix(rows, columns)

        print("\nOriginal Matrix:")
        display_matrix(matrix)
        print("\nTransposed Matrix:")
        display_matrix(transpose_matrix(matrix))

    elif choice == "2":
        rows = int(input("Enter number of rows: "))
        columns = int(input("Enter number of columns: "))

        print("\nEnter Matrix A:")
        matrix_a = read_matrix(rows, columns)
        print("\nEnter Matrix B:")
        matrix_b = read_matrix(rows, columns)

        print("\nSum:")
        display_matrix(add_matrices(matrix_a, matrix_b))

    elif choice == "3":
        rows_a = int(input("Enter the number of rows in Matrix A: "))
        columns_a = int(input("Enter the number of columns in Matrix A: "))
        columns_b = int(input("Enter the number of columns in Matrix B: "))

        print("\nEnter Matrix A:")
        matrix_a = read_matrix(rows_a, columns_a)
        print("\nEnter Matrix B:")
        matrix_b = read_matrix(columns_a, columns_b)

        print("\nProduct:")
        display_matrix(multiply_matrices(matrix_a, matrix_b))

    else:
        print("Error: Please choose an operation from 1 to 3.")


if __name__ == "__main__":
    main()
