

from collections import deque

graph = dict()    # 定义字典
graph['your'] = ['alice', 'boob', 'claire']
graph['boob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []


def person_is_seller(name):
    return name[-1] == 'm'   # 终止条件


def search(graph):
    search_queue = deque()   # 创建队列
    search_queue += graph["your"]    # your内的元素添加到队列
    searched = []    # 建立防止重复措施

    while search_queue:
        person = search_queue.popleft()   # 返回列表中的第一个元素并删除列表中数值
        if person not in search_queue:     # 防止重复
            if person_is_seller(person):
                print(searched)
                print(person + ' is a mango seller')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


def abc(graph):    # 寻找最短路径
    queue1 = [('your', ['your'])]   # 定义一个队列 ，包含yuor和路径
    while queue1:
        (a, b) = queue1.pop(0)    # 将队列的值your赋予a，【your】赋予b
        for next1 in graph[a]:    # 字典a相关的路径名字进行循环
            if person_is_seller(next1):  # 寻到终止条件则返回路径
                h = b + [next1]
            else:
                queue1.append((next1, b + [next1]))   # 没到终止条件 队列增加  路径b和a更新
    return h


print(abc(graph))
