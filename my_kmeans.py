"""
1.如何实现kmeans
2.如何确定k到个数
3.如何评估聚类效果
"""

import numpy as np
import random
import matplotlib.pyplot as plt

# 构造数据点
data = np.random.randint(1,100,size=(100,2))

k = 3

def kmean(data, k):
    # 初始化初始中心
    initial_centers = random.sample(list(data),k)
    centers = np.array(initial_centers)

    max_iters = 100

    for iter in range(max_iters):
        clusters = [[] for _ in range(k)]

        # 计算欧氏距离
        for point in data:
            # 计算点point到各个中心的距离, 将其加入最近的cluster
            distances = [np.linalg.norm(point - center) for center in centers]
            cluster_idx = np.argmin(distances)
            clusters[cluster_idx].append(point)
        
        new_centers = [np.mean(cluster,axis=0) for cluster in clusters] # axis=0 行; axis=1 列

        if np.array_equal(centers, new_centers):
            break

        centers = new_centers 

    return centers

centers = kmean(data=data, k=k)

# 在坐标中画出各点和中心
x = [point[0] for point in data]
y = [point[1] for point in data]
plt.scatter(x,y,c='blue',marker='o')
c_x = [point[0] for point in centers]
c_y = [point[1] for point in centers]
plt.scatter(c_x,c_y,c='red',marker='x')
plt.show()