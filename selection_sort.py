import sys
# 选择排序
'''
从列表中选出最大值或者最小值，存放在列表的起始位置
不稳定
最好情况:O(n^2)
最坏情况:O(n^2)
平均情况:O(n^2)
辅助情况：O(1)
'''
def selection_sort(l):
    for i in range(len(l)):
        for j in range(i,len(l)):
            if l[i] > l[j]:
                l[i],l[j] = l[j],l[i]
    return l
if __name__ == '__main__':
    l = [6,2,7,3,8,9]
    results = selection_sort(l)
    sys.stdout.write(str(results))