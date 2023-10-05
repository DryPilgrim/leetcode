"""
knn(k-nearest neighbor), 顾名思义，找到最近的k个邻居，在前k个邻居中选择占比最高的类别作为预测类别。
由上可知，knn的精度取决于两方面：1.实际计算的距离；2，k的选择。
knn常用的两种距离度量方式：l2范数（欧氏距离）；l1范数（曼哈顿距离）。
"""

import numpy as np
import matplotlib.pyplot as plt

def create_dataset():
    #训练集数据
    # group = np.array([[1.0, 2.0], [1.2, 0.1], [0.1, 1.4], [0.3, 3.5], [1.1, 1.0], [0.5, 1.5]])
    group1 = np.random.randint(1,10,size=(10,2))
    group2 = np.random.randint(10,20,size=(10,2))
    group3 = np.random.randint(20,30,size=(10,2))
    group  = np.concatenate((group1,group2,group3),axis=0)
    #训练集标签
    labels1 = np.array(['A']*10)
    labels2 = np.array(['B']*10)
    labels3 = np.array(['C']*10)
    labels = np.concatenate((labels1,labels2,labels3),axis=0)
    return group, labels

def calc_dis(dis, i, x_train, x_test):
    assert dis == 'E' or dis == 'M', 'dis must be E or M'
    if dis == 'E': #计算欧式距离
        # d = np.sqrt(np.sum(((x_train - np.tile(x_test[i], (x_train.shape[0], 1))) ** 2), axis=1))
        d = np.sqrt(np.sum(((x_train - x_test[i]) ** 2), axis=1))
    if dis == 'M': #计算曼哈顿距离
        # d = np.sum(abs(x_train - np.tile(x_test[i], (x_train.shape[0], 1))), axis=1)
        d = np.sum(abs(x_train - x_test[i]), axis=1)
    return d

def knn(k, dis, x_train, y_train, x_test):
    num_test = x_test.shape[0]
    label_list = []
    for i in range(num_test):
        #计算测试集中待分类的对象与训练集中每个对象的距离
        d = calc_dis(dis, i, x_train, x_test)
        """np.argsort :: 返回升序排序后数组中各元素在原数组中的索引。
        ---
        arr = np.array([3, 1, 2, 4, 5])
        # 返回按升序排序后的索引
        sorted_indices = np.argsort(arr)
        print(sorted_indices) # [1 2 0 3 4]
        ---
        为什么结果是[1 2 0 3 4]？
        原始数组 arr 是 [3, 1, 2, 4, 5]。
        首先，np.argsort 函数找到数组中最小的元素，也就是 1。在原始数组中，1 的索引是 1，所以结果的第一个元素是 1。
        接下来，找到第二小的元素，也就是 2。在原始数组中，2 的索引是 2，所以结果的第二个元素是 2。
        接下来，找到第三小的元素，也就是 3。在原始数组中，3 的索引是 0，所以结果的第三个元素是 0。
        """
        nearest_k = np.argsort(d) # 将d的元素从小到大排序得到d', d'中各元素在原数组d中的索引index，nearest_k存储的就是index
        #计算距离测试集对象最近的k个训练集对象所属类别的占比
        top_k = nearest_k[:k] # 距离测试集对象最近的k个训练集对象的索引index
        class_count = {}
        for j in top_k:
            class_count[y_train[j]] = class_count.get(y_train[j], 0) + 1 # class_count: {'A': 3}
        #占比最高的类别即为测试集对象的类别
        sorted_class_count = sorted(class_count.items(), reverse=True) # sorted_class_count: [('A', 3)]
        label_list.append(sorted_class_count[0][0])
    return np.array(label_list)

group, labels = create_dataset()
# print(group[:5,:]) #取array的前5行所有列
# print(labels == 'A') #[ True  True  True  True  True  True  True  True  True  True False False False False False False False False False False False False False False False False False False False False]
plt.scatter(group[labels == 'A', 0], group[labels == 'A', 1], color='r', marker='*')
plt.scatter(group[labels == 'B', 0], group[labels == 'B', 1], color='r', marker='o')
plt.scatter(group[labels == 'C', 0], group[labels == 'C', 1], color='r', marker='+')
x_test = np.random.randint(1,30,size=(3,2))
y_test_pred1 = knn(3, 'E', group, labels, x_test)
y_test_pred2 = knn(3, 'M', group, labels, x_test)
plt.scatter(x_test[:,0],x_test[:,1],marker='x', c='blue')
print(y_test_pred1,  y_test_pred2)
plt.show()
