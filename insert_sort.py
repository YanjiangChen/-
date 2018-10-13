import random
# 插入排序
'''
类似于冒泡排序，只不过从最后一个元素开始交换

时间复杂度：O（n^2)
'''
def insert_sort(num_list):
    for i in range(len(num_list)):
        for j in range(i,0,-1):
            if num_list[j] < num_list[j-1]:
                num_list[j],num_list[j-1] = num_list[j-1],num_list[j]
    return num_list

if __name__ == '__main__':
    num_list = random.sample(range(100),5)     #在指定序列中随机获得指定长度片段
    print(insert_sort(num_list))