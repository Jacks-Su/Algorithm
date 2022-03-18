# 递归计算列表元素数


def numArr(Arr):

    if len(Arr) == 0:
        num = 0
        return num

    else:
        Arr.pop(0)
        num = 1 + numArr(Arr)
        return num


Arr = [1, 2, 3, 4, 5, 7, 8]  # 实例
a = []    # 实例
print(numArr(a))
