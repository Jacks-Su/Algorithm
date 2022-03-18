# 递归计算列表的和

def Sum(Arr):
    if len(Arr) == 0:
        sum = 0
        return sum
    else:
        sum = Arr.pop(0) + Sum(Arr)
        return sum


Arr = [1, 2, 3, 5, 100, 20, 40]
a = []

print(Sum(a))
