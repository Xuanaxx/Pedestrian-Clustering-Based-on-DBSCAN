import random
import numpy as np
import math
import copy


# 计算两个点之间的欧式距离，参数为两个数组坐标
def dist(t1, t2):
    dis = math.sqrt((np.power((t1[0] - t2[0]), 2) + np.power((t1[1] - t2[1]), 2)))
    # print("两点之间的距离为："+str(dis))
    return dis


# t1 = np.array([1, 2])
# t2 = np.array([3, 4])
# print(dist(t1, t2))


# DBSCAN算法，参数为数据集，Eps为指定半径参数，MinPts为制定邻域密度阈值,包括点本身
def dbscan(Data, Eps, MinPts):
    num = len(Data)  # 点的个数
    # print("点的个数："+str(num))
    C = [-1 for i in range(num)]  # C为输出结果，默认是一个长度为num的值全为-1的列表
    # 用k来标记不同的簇，k = -1表示噪声点
    k = -1
    unvisited = set([i for i in range(num)])  # 没有访问到的点的列表
    Nei_list = []  # 存储每个数据点邻域点
    coreset = []  # 核心点集
    for j in range(num):
        # N为xj的epsilon邻域中的对象的集合
        N = []
        for i in range(num):
            if (dist(Data[i], Data[j]) <= Eps):
                N.append(i)
        Nei_list.append(N)
        if len(N) >= MinPts:
            coreset.append(j)
    coreset = set(coreset)
    while len(coreset) != 0:
        old = copy.deepcopy(unvisited)
        o = random.choice(list(coreset))
        Q = []
        Q.append(o)
        unvisited.remove(o)
        while len(Q) != 0:
            q = Q[0]
            Q.remove(q)
            # Nei为q的epsilon邻域中的对象的集合
            Nei = set(Nei_list[q])
            delta = Nei & unvisited  # delta为q的epsilon邻域与未访问点集的交集
            Q = Q + list(delta)
            unvisited = unvisited - delta
        k = k + 1
        Ck = old - unvisited
        for i in Ck:
            C[i] = k
        coreset = coreset - Ck
    return C
