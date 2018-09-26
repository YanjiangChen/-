import sys

# 冒泡排序
'''
比较列表中相邻的元素
稳定的排序算法
时间复杂度：
最坏情况：O(n^2)
最好情况：O(n^2)
平均时间:O(n)
辅助空间：O(1)
'''
def bubble_sort(l):
    for i in range(len(l)):
        for j in range(i,len(l)-1):
            if l[j] > l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]
    return l
if __name__ == '__main__':
    l = [6,2,7,3,8,9]
    results = bubble_sort(l)
    sys.stdout.write(str(results))