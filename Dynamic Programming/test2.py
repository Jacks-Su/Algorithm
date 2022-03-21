a = ["b", "l", 'u', 'e']
b = ['c', 'l', 'u', 'e', 's']

cell = [[0 for j in range(len(b)+1)] for i in range(len(a)+1)]

print(cell[0][0])
for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        if a[i-1] == b[j-1]:
            cell[i][j] = cell[i-1][j-1] + 1
        else:
            cell[i][j] = max(cell[i-1][j], cell[i][j-1])
print(cell)
