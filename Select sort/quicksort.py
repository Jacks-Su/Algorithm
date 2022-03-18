# 快速排序

def quickSort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        great = [i for i in arr[1:] if i > pivot]
        return quickSort(less) + [pivot] + quickSort(great)


Arr = [70, 6, 20, 4, 5, 7, 8]  # 实例

print(quickSort(Arr))
