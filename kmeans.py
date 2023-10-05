import numpy as np
import random
import matplotlib.pyplot as plt
"""
1.实现kmeans;
2.如何确定k值？
  1）肘部法则（Elbow Method）：每个点到其所属族中心的距离的总和。
  2）轮廓分析（Silhouette Analysis）：
    point到当前族中各点的平均距离a, 到其余族中最近族中各点的平均距离b, 轮廓系数 g = (b-a)/max(a,b), -1<g<1.
    g月接近1, 聚类效果越好。
3.如何评估聚类效果？
  轮廓分析。
"""

# 生成示例数据
np.random.seed(0)
X1 = np.random.uniform(1,3,(30, 2)) #<class 'numpy.ndarray'>
X2 = np.random.uniform(4,6,(39,2))
X3 = np.random.uniform(7,10,(20,2))
X = np.concatenate((X1, X2, X3), axis=0)
x = [point[0] for point in X]
y = [point[1] for point in X]
plt.scatter(x,y,marker='o',c='blue')

# print(X)       # [[2.09762701 2.43037873] [2.20552675 2.08976637] [1.8473096  2.29178823] [1.87517442 2.783546  ]]
# print(list(X)) # [ array([2.09762701, 2.43037873]), array([2.20552675, 2.08976637]), array([1.8473096 , 2.29178823]) ]

# 定义K值
K = 3

# 随机初始化聚类中心
initial_centers = random.sample(list(X), K)
centers = np.array(initial_centers)

# print(centers) # [[5.04649611 4.18788102] [4.12829499 5.38494424] [2.09762701 2.43037873]]

# 定义最大迭代次数
max_iters = 100
for _ in range(max_iters):
    # 分配数据点到最近的聚类中心
    clusters = [[] for _ in range(K)]
    for point in X:
        # 计算两坐标相减结果的l2范数（两点的距离）
        distances = [np.linalg.norm(point - center) for center in centers]
        cluster_idx = np.argmin(distances)
        clusters[cluster_idx].append(point)

    # 计算新的聚类中心
    new_centers = [np.mean(cluster, axis=0) for cluster in clusters]

    # 判断是否收敛
    if np.array_equal(centers, new_centers):
        break

    centers = new_centers

c_x = []
c_y = []
# 打印最终的聚类中心
print("Final Cluster Centers:")
for i, center in enumerate(centers):
    print(f"Cluster {i+1}: {center}")
    c_x.append(center[0])
    c_y.append(center[1])

plt.scatter(c_x, c_y, c='red', marker='x')
# 显示图例
plt.legend()
# 显示图形
plt.show()