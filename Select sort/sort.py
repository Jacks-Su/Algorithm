# 排序

def findSmallest(arr):   # 寻找最小值
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionSort(arr):   # 选择排序
    newArr = []      # 建立空列表
    for i in range(len(arr)):
        smallest = findSmallest(arr)    # 寻找数组最小值索引
        newArr.append(arr.pop(smallest))  # 空列表中添加最小值，arr.pop（）：删除数组中索引所表示的值，并返回那个值
    return newArr


ss = [5, 5, 3, 6, 7, 8, 9, 10, 20]   # 例子

print(selectionSort(ss))
