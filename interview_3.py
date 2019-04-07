import numpy as np

'''
对于在一个每一行从左到右依次递增，每一列从上到下依次递增的二维数组查找一个元素，
可以选择从数组左上角开始查找array[i][j]，如果目标元素大于array[i][j]，i+=1，
如果元素小于array[i][j]，j-=1，依次循环直至找到这个数。

时间：2019.04.07
作者：王小米
'''
class Solution:
    # array 二维数组
    def Find(self,array,target):

        #print(array)
        if array == []:
            return False

        rows = len(array)   #行数
        cloumns = len(array[0]) #列数
        print(rows,cloumns)

        i = 0
        j = cloumns -1

        while i<rows and j>=0:
            print(array[i][j])
            if array[i][j] == target:      # 与target相等则返回true
                return True
                break
            elif array[i][j]> target:     # 右上角第一个数大于target 则删除对应列
                j -= 1
            else:                         # 右上角小于target 则删除对应行
                i += 1
        return False

    # 统计target出现的次数
    def count(self,array,target):
        rows = len(array)   #行数
        cloumns = len(array[0]) #列数
        row,col = 0,cloumns-1  #初始化行列
        count = 0
        while row<rows and col>=0:
            print(array[row][col])
            if array[row][col] == target:  # 重复次数累加
                count +=1
                row += 1
            elif array[row][col] > target:
                col -= 1
            else:
                row += 1
        return count

S = Solution()
#array = input()
#target = input()
array = [[1, 2, 8, 9],
         [2, 4, 9, 12],
         [4, 7, 10, 13],
         [6, 10, 11, 15]]
print(S.Find(array,10))
print(S.count(array,10))


