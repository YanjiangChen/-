import sys

# 快速排序
'''
第一次排序结束后基准值左边的值小于基准值，基准值后边的值都大于基准值
不稳定
最坏情况：O(n^2)
最好情况：O(nlogn)
平均时间：O(nlogn)
辅助空间：O(lgn)
'''
def l_sort(l):
    if len(l) < 2:
        return l
    else:
        num = l[0]
        less = [i for i in l[1:] if i < num]
        greater = [j for j in l[1:] if j > num]
    return l_sort(less) + [num] + l_sort(greater)

if __name__ == '__main__':
    l = [6,2,7,3,8,9]
    results = l_sort(l)
    sys.stdout.write(str(results))