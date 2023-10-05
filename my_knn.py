import numpy as np
import matplotlib.pyplot as plt

k = 3

# 构造训练数据
group1 = np.random.randint(1,10,size=(10,2))
label1 = np.array(['A']*len(group1))
group2 = np.random.randint(10,20,size=(10,2))
label2 = np.array(['B']*len(group2))
group3 = np.random.randint(20,30,size=(10,2))
label3 = np.array(['C']*len(group3))

x_train = np.concatenate((group1,group2,group3),axis=0)
labels = np.concatenate((label1,label2,label3),axis=0)

# 构造测试数据
x_test = np.random.randint(1,40,size=(3,2))
labels_pred = []

# 计算各测试样本到各训练样本之间的距离
for x in x_test:
    distances = np.sqrt(np.sum((x_train - x)**2,axis=1)) ##注意⚠️：axis=1/0 代表着分别按 行/列 求和。
    ## 计算升序排序后的index
    nearest = np.argsort(distances)
    ## 计算最近的的k个index
    nearest_k = nearest[:k]
    ## 统计nearest_k中各个类别的数目
    class_cnt = {}
    for i in nearest_k:
        class_cnt[labels[i]] = class_cnt.get(labels[i], 0) + 1
    sorted_class_cnt = sorted(class_cnt.items(), reverse=True)
    labels_pred.append(sorted_class_cnt[0][0])
labels_pred = np.array(labels_pred)
print(x_test,labels_pred)

# 画图
plt.scatter(x_train[labels == 'A', 0],x_train[labels == 'A', 1],marker='+', c='blue') ##注意⚠️：x_train[labels == 'A', 0]这种取值方法
plt.scatter(x_train[labels == 'B', 0],x_train[labels == 'B', 1],marker='.', c='blue')
plt.scatter(x_train[labels == 'C', 0],x_train[labels == 'C', 1],marker='o', c='blue')
plt.scatter(x_test[:,0], x_test[:,1],marker='*',c='red')
plt.show()