import numpy as np
# np.set_printoptions(formatter={'float_kind': '{:.2f}'.format})
# Uncommenting the line above will print all
# floats in ndarrays with only 2 decimal places.

# Task 1
print('Task 1')
# 1
m = np.array([[  2,  1,  3,  1, -2,  1],
              [  1, -3, -4, 10,  4,  2],
              [  1,  2,  3,  4,  5,  6],
              [  2,  0,  2,  0,  3,  1],
              [  1,  2,  3,  3,  2,  1],
              [  5,  1,  6,  1, -7, -2]])

v = np.array([1, -4, 2, 2, 1, 8])
print('#1:', np.matmul(m, v), sep='\n')
print()

# 2
m1 = np.array([[  2,  1,  3,  1, -2,  1],
               [  1, -3, -4, 10,  4,  2],
               [  1,  2,  3,  4,  5,  6],
               [  2,  0,  2,  0,  3,  1],
               [  1,  2,  3,  3,  2,  1]])

m2 = np.array([[  2,  1,  3,  1],
               [  1, -3,  4,  2],
               [  3,  4,  5,  6],
               [  2,  0,  2,  1],
               [  1,  2,  2,  1],
               [  5,  1,  1, -2]])
print('#2:', np.matmul(m1, m2), sep='\n')
print()

# 3
m = np.array([[  2,  1,  3,  1],
              [  1, -3,  4,  2],
              [  3,  4,  5,  6],
              [  2,  0,  2,  1],
              [  1,  2,  2,  1],
              [  5,  1,  1, -2]])
print('#3:', m.transpose(), sep='\n')
print()

# 4
m = np.array([[  2,  1,  4,  1,  9,  1],
              [  1, 36,  4, 10,  4,  2],
              [  1,  2,  3,  4,  5,  6],
              [  2,  0,  2,  0,  3,  1],
              [  1,  2,  3,  3,  2,  1],
              [  5,  1,  6,  1,  9, 25]])
print('#4:', np.sqrt(m), sep='\n')
print()

# 5
m = np.array([[  2,  1,  3,  1, -2,  1],
              [  1, -3, -4, 10,  4,  2],
              [  1,  2,  3,  4,  5,  6],
              [  2,  0,  2,  0,  3,  1],
              [  1,  2,  3,  3,  2,  1],
              [  5,  1,  6,  1, -7, -2]])
print('#5:', np.sum(m), sep='\n')
print()

# 6
m1 = np.array([[  1,  2,  1,  2],
               [  2, -4,  1,  0],
               [  0,  0, -1,  0],
               [  0,  0,  0,  5]])
print('#6:', f'{np.linalg.det(m1):.2f}', sep='\n')
print()

def format_sol(sol):
    formatted_sol = ''
    for i, val in enumerate(sol):
        formatted_sol += f'{chr(122-len(sol)+i+1)}: {val:.2f}\n'
    return formatted_sol

# Task 2
print('Task 2')
a1 = np.array([[  1,  1,  1],
              [  1,  2,  2],
              [  2,  3, -4]])
b1 = np.array([6, 11, 3])
print('System 1:', format_sol(np.linalg.solve(a1, b1)), sep='\n')


a2 = np.array([[  1,  2, -1,  1],
               [ -1,  1,  2, -1],
               [  2, -1,  2,  2],
               [  1,  1, -1,  2]])
b2 = np.array([6, 3, 14, 8])
print('System 2:', format_sol(np.linalg.solve(a2, b2)), sep='\n')