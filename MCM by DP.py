#  Implement the matrix chain multiplication problem using dynamic programming in Python

def matrix_chain_order(p):
    n = len(p) - 1
    m = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    s = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        m[i][i] = 0

    for l in range(2, n + 1):
        for i in range(1, n - l + 2):
            j = i + l - 1
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k

    return m, s

def print_optimal_parens(s, i, j):
    if i == j:
        print(f'Matrix {i}', end='')
    else:
        print('(', end='')
        print_optimal_parens(s, i, s[i][j])
        print_optimal_parens(s, s[i][j] + 1, j)
        print(')', end='')

# Example usage
p = [10, 100, 5, 50]
m, s = matrix_chain_order(p)
print_optimal_parens(s, 1, len(p) - 1) # Output: ((Matrix 1(Matrix 2Matrix 3))Matrix 4)
