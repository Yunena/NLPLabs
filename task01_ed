# -*- coding: UTF-8 -*-
import numpy as np


s1 = input("请输入第一句话：")
s2 = input("请输入第二句话：")
l1 = len(s1)
l2 = len(s2)
ed = np.zeros([l1+1,l2+1], dtype = int)



i = 1
j = 1
while(i<=l1):
    ed[i][0]=i
    i+=1
while(j<=l2):
    ed[0][j]=j
    j+=1
i = 0
j = 0
x = 0
y = 0
while(i<l1):
    j = 0
    while(j<l2):
        if(s1[i]==s2[j]):
            ed[i+1][j+1]=ed[i][j]
        elif (i>0 and j>0 and i<l1-1 and j<l2-1 and s1[i-1]==s2[j] and s1[i]==s2[j-1]):
                ed[i+1][j+1]=1+min(ed[i-1][j-1],ed[i+1][j],ed[i][j+1])

        else:
            ed[i+1][j+1]=1+min(ed[i][j],ed[i+1][j],ed[i][j+1])
        j+=1
    i+=1

print("编辑距离：", ed[l1][l2])
print(ed)
