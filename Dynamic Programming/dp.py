# 动态规划  在总量确定下寻找总价值最大的物品  最大是多少

n = 4  # 物品数量（种类）
w = [2, 3, 4, 5]   # （种类的重量）
v = [3, 4, 5, 6]   # 物品的价值
c = 8    # 总重量
value = [[0 for j in range(c+1)] for i in range(n+1)]   # 创建规划表  需要多一个零的行列做数据缓冲
# print(value)
# 定义  i j 为行和列
for i in range(1, n+1):
    for j in range(1, c+1):
        if j-w[i-1] >= 0:
            value[i][j] = max(v[i-1] + value[i-1][j-w[i-1]], value[i-1][j])
        else:
            value[i][j] = value[i-1][j]
# 打印动态规划表
for x in value:
    print(x)
# 输出最大值
print("最大的价值为：", value[n][c])
#  包内最大值时所包含的物品: 如果当前的物品加入包中，那么当前总价值大于前一行的总价值
#  即最后一行最后一个数据和上一行的最后一个数据做对比，不相等即加入了最后一个物品
#  最后一个物品的重量在背包中被减去那么下次对比的数据就是剩余重量中的每行的最大价值
#  在本例中 最后一行10>上一行9 即最后一个物品加入 重量5 那么剩余重量3  第三行和第四行重量为3时相等即第三个物品没加入
#  依次递推
a = [0 for i in range(n)]
j = c
for i in range(n, 0, -1):
    if value[i][j] > value[i-1][j]:
        a[i-1] = 1
        j -= w[i-1]
for i in range(n):
    if a[i] == 1:
        print("第", i+1, "个物品加入包中,它的价值为：", v[i])
