import numpy as np

persons=np.random.randint(1,100,(100,17,2))
# index=[key for key in range(len(persons))]#人的index
index=[0]*len(persons) #人的index
# persons_=np.concatenate((persons,index),axis=0)

# out (1000,1)

def find_node(persons,index):
    """
    1000个人,每个人17个关键点,写代码实现:手举高过头顶的人有哪些?
    head 取第0个点
    hands 取1-3个点
    """
    idx=-1
    for person in persons:
        head = person[0,1]
        hands = person[1:4,:]
        idx+=1
        for node in hands:
            if node[1] >= head:
                index[idx]=1
    return index

index_res=find_node(persons,index)
index_res = np.array(index_res)
print("1000个候选者中手举超过头顶的人的索引:\n",index_res)


# print("1000个候选者中手举超过头顶的人的索引:\n")
# print(np.argwhere(index_res==-1)) #np.argwhere(array==-1),array为np.numpy类型