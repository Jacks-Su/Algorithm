# from collections import deque
graph = dict()
#  权重这个说话并不严谨 理解.jpg
graph["yp"] = {}
graph["yp"]["cp"] = 5   # 字典包含每个节点到下一个节点的权重以及节点和节点的连接单向
graph["yp"]["hb"] = 0

graph["cp"] = {}
graph["hb"] = {}
graph["cp"]["gt"] = 15
graph["cp"]["jzg"] = 20
graph["hb"]["gt"] = 30
graph["hb"]["jzg"] = 35

graph["gt"] = {}
graph["jzg"] = {}
graph["gt"]["gq"] = 20
graph["jzg"]["gq"] = 10

graph["gq"] = {}

parents = {}                # 子系：父系   开头和未知的
parents["cp"] = "yp"
parents["hb"] = "yp"
parents["gq"] = None

infinity = float("inf")
costs = {}
costs["cp"] = 5    # 从起点到终点的权重，开始是已知的，过程节点是未知的，设置为最大   程序运行完会显示 全部权重
costs["hb"] = 0
costs["gt"] = infinity
costs["jzg"] = infinity
costs["gq"] = infinity

processed = []   # 记录处理过的节点


def find_lowest_cost_node(costs):   # 寻找权重最小的节点   将每个节点的数据进行对比，小的提出并返回
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


node = find_lowest_cost_node(costs)
while node is not None:                        # 循环
    cost = costs[node]                       # cost 节点的权重   neig节点的子系
    neig = graph[node]

    for n in neig.keys():         # 节点子系循环
        new_cost = cost + neig[n]    # 初始点到节点再到节点子系的权重和
        if costs[n] > new_cost:         # 更新初始到当前节点的总权重
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)    # 添加记录点
    node = find_lowest_cost_node(costs)

print(costs)
print(parents)
