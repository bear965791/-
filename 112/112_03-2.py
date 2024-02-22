# //為除法運算,只取整數部分
def op(data, x, y, n):
    sum = 0
    for i in range(x, x+n):
        for j in range(y, y+n):
            sum = sum +______
    return sum//__

def compress(data, m, n):
    size = __
    target = []
    for x in range(size):
        row = []
        for y in range(size):
            row.append(op(data, x*n, y*n, n))
        target.append(row)
    return target

data = [[1, 2, 3, 4, 5, 6, 7],
        [8, 9, 10, 11, 12, 13, 14],
        [15, 16, 17, 18, 19, 20, 21],
        [22, 23, 24, 25, 26, 27, 28],
        [29, 30, 31, 32, 33, 34, 35],
        [36, 37, 38, 39, 40, 41, 42],
        [43, 44, 45, 46, 47, 48, 49]]

print(compress(data, 4, 2), '\n##')
print(compress(data, 6, 2), '\n##')
print(compress(data, 6, 3), '\n##')