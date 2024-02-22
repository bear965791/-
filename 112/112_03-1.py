#不要在逗號, 分號, 冒號前面加空格, 但應該在它們後面加(除了在行尾).
#二元操作符兩邊都加上一個空格

#取1-n中可被2整除的數字
def f1(n):
    X = [ i for i in range (1, n) if  i % 2 == 0]
    return X

#創建空的dictionary,每個字元當作key值,value為該字元數量
def f2(S):
    data = dict()
    for s in S:
        if s in data.keys():
            data[s] = data[s] + 1
        else:
            data[s] = 1
    return data

def f3(n):
    f = lambda m, n: m * n + 1
    X = {i: f(i, i+1) for i in range (1, n) if i % 3 == 0}  #此時X型別為dict
    return X

def f4():
    scores = [['John', 90, 80], ['Bob', 50, 70], ['Mary', 80, 70]]
    data = filter(lambda x: True if sum(x[1:3]) < 150 else False, scores)
    return list(data)

def f5(s1, s2, m, n):
    return s1[m:n] + s2[m:n]

def f6(A, B):
    return list(map(lambda x, y: x **y, A, B))

def f7(data, n):
    if n == len(data): return [data]
    elif n == 0: return ['']
    s0 = f7(data[1:], n)
    s1 = [data[0] + s for s in f7(data[1:], n-1)]
    return sorted(s0 + s1)

print(f1(8)[2])
print(f2('ntut csie')['t'])
print(f3(6)[3])
print(f4())
print(f5('ntut', 'good', 2, 4))
print(f6([2, 4, 6], [3, 2, 1]))
print(f7('abc', 2)[2])