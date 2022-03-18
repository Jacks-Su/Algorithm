# 计算方块最大，...

def MAXq(arr):

    if arr[0] % arr[1] == 0:
        return arr[1]             # return 栈相关
    else:
        d = arr[0] % arr[1]
        arr = [arr[1], d]
        # print(c)
        return MAXq(arr)   # 推一下流程


arr = [1680, 640]

print(MAXq(arr))
