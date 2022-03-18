# 递归列表最大值


def maxNumber(Arr):
    a = Arr.pop(0)
    if len(Arr) == 0:
        return a

    b = maxNumber(Arr)
    if a > b:
        return a
    else:
        return b


Arr = [1, 2, 12, 4, 5, 7, 8]  # 实例
a = []    # 实例

print(maxNumber(Arr))
