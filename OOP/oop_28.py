from matrix import *


def main():
    mat = Matrix(a=1, b=10)
    print(mat)
    print(mat.sum_matrix())
    print(mat.max_element())
    print(mat.min_element())
    mat2 = Matrix(mat)
    print(mat2)
    print(matrix_sum_matrix(mat2))
    print(matrix_max_element(mat2))
    print(matrix_min_element(mat2))


if __name__ == '__main__':
    main()
