from dbscan0 import *
import pandas as pd
import matplotlib.pyplot as plt

# 读取行人轨迹坐标点
Allpoints = pd.read_csv('TrajectoryData_students003/students003.txt', sep='\t',
                        names=['Timestep', 'ID', 'X', 'Y'], header=None)
# 获得每一帧的行人坐标位置,共541帧
frame = []
for i in range(0, 541):
    timei = (Allpoints["Timestep"] == i * 10)  # 第i帧的时间
    framei = Allpoints.loc[timei, "X":"Y"].values  # 第i帧时各行人的坐标位置
    frame.append(framei)
# print(frame[0][0])
# print(len(frame[0]))


k_dist = []  # k距离，取k=2
Dist = np.zeros((len(frame[0]), len(frame[0])))
for j in range(len(frame[0])):
    for k in range(len(frame[0])):
        Dist[j][k] = dist(frame[0][j], frame[0][k])
    Dist[j].sort()
    k_dist.append(Dist[j][2])
k_dist.sort()
x = [i for i in range(len(frame[0]))]
plt.figure()
plt.scatter(x, k_dist)
plt.show()

eps = 1.1
min_Pts = 2
for i in range(0, 541):
    C = dbscan(frame[i], eps, min_Pts)
    plt.figure()
    plt.scatter(frame[i][:, 0], frame[i][:, 1], c=C)
    plt.axis('off')
    f = plt.gcf()
    f.savefig(r'img_ori\{}.png'.format(i))  # 保存第i帧聚类结果图
    plt.show()
    plt.close()
