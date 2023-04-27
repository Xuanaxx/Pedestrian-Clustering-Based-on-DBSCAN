from dbscan0 import dbscan
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter


def most(list):  # 寻找最大频数的类
    count = Counter(list)
    k = list[0]
    for key in count.keys():
        if count[key] > count[k]:
            k = key
    return k


def find(IDk, x):  # 在第t帧中寻找ID为x的人
    for i in range(IDk.shape[0]):
        if IDk[i] == x:
            return i  # 返回他的索引
    return -1


def union_clustering(C, ID, k):
    for i in range(len(C)):  # i为帧数
        for j in range(len(C[i])):  # j为第i帧内的第j个人
            cluster = []
            for t in range(max(i - k, 0), min(i + k + 1, len(C))):  # 只考虑第i帧前后k帧的联系
                l = find(ID[t], ID[i][j])  # 如果第t帧内存在第i帧内第j个人
                if l >= 0:
                    cluster.append(C[t][l])  # 如果第t帧内存在第i帧内第j个人，则该人在第t帧所属类的得分加1
            C[i][j] = most(cluster)  # 取出现频数最高的类作为第i帧第j个人的聚类簇
    return C


# 读取行人轨迹坐标点
Allpoints = pd.read_csv('TrajectoryData_students003/students003.txt', sep='\t',
                        names=['Timestep', 'ID', 'X', 'Y'], header=None)

# 获得每一帧的行人坐标位置,共541帧
frame = []
ID = []
for i in range(0, 541):
    timei = (Allpoints["Timestep"] == i * 10)  # 第i帧的时间
    framei = Allpoints.loc[timei, "X":"Y"].values  # 第i帧时各行人的坐标位置
    frame.append(framei)
    IDi = Allpoints.loc[timei, "ID"].values  # 第i帧时各行人的ID
    ID.append(IDi)
# print(frame[0][0])
# print(len(frame[0]))
# print(ID[0])

eps = 1.1
min_Pts = 2
C = []
for i in range(0, 541):
    C.append(dbscan(frame[i], eps, min_Pts))
C_union = union_clustering(C, ID, 3)
for i in range(0, 541):
    plt.figure()
    plt.scatter(frame[i][:, 0], frame[i][:, 1], c=C_union[i])
    plt.axis('off')
    f = plt.gcf()
    f.savefig(r'img_update\{}.png'.format(i))
    plt.show()
    plt.close()
