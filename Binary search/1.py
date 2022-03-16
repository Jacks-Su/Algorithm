

def binary_search(list, item):   # 列表从大到小排列
    low = 0      # 列表下限索引0
    high = len(list) - 1   # 列表最大值的索引

    while low <= high:    # 判定排除单个元素
        mid = int((low + high) / 2)   # 列表中间元素的索引且为整数
        guess = list[mid]   # 列表中间索引的值

        if guess == item:    # 相等则返回索引
            return mid
        elif guess > item:   # 中间的值大于需要的值那么更新索引范围，上限变为中间值
            high = mid - 1
        else:
            low = mid + 1    # 相反
    return None


my_list = [1, 3, 4, 5, 7, 8, 10]
print(binary_search(my_list, 7))
