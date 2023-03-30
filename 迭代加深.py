#请将附件放在桌面并且更改下方路径的用户名
#下面两个库可以将这个迷宫可视化
import matplotlib.pyplot as plt
import numpy as np
import time
time1=time.perf_counter()
#以下变量作为全局变量易于DFS算法
matrix=[]#迷宫矩阵
track=[]
sline=int(0)
scol=int(0)
line=int(0)
col=int(0)
linenum=int(18)
colnum=int(36)
def DFS_limit(lim,pre):#受限DFS，回溯
    global matrix,sline,scol,line,col,track
    if(lim==0) :
        return bool(False)
    
    if matrix[line][col]=='E':
        return bool(True)
    if len(track)>=lim:
        return bool(False)

    if pre!=3 and col!=0 and matrix[line][col-1]!='1':
        col-=1
        track.append(int(1))
        if DFS_limit(lim,1):
            return bool(True)
        col+=1
        track.pop(len(track)-1)
    if pre!=4 and line!=17 and matrix[line+1][col]!='1':
        line+=1
        track.append(int(2))
        if DFS_limit(lim,2):
            return bool(True)
        line-=1
        track.pop(len(track)-1)
    if pre!=1 and col!=35 and matrix[line][col+1]!='1':
        col+=1
        track.append(int(3))
        if DFS_limit(lim,3):
            return bool(True)
        col-=1
        track.pop(len(track)-1)
    if pre!=2 and line!=0 and matrix[line-1][col]!='1':
        line-=1
        track.append(int(4))
        if DFS_limit(lim,4):
            return bool(True)
        line+=1
        track.pop(len(track)-1)

    return bool(False)

##main 函数
s=[]
f=open("C:\\Users\\LHH\\Desktop\\MazeData.txt")    ##文件路径
for i in range(linenum):
    st=f.readline()
    s=[]
    for j in range(colnum):
        s.append(st[j])
    matrix.append(s)
##18行36列
    
for i in range(linenum):
    for j in range(colnum):
        if matrix[i][j]=='S':
            sline=i
            scol=j
##得到起点坐标 (sline,scol)

for limit in range(linenum*colnum):##迭代加深
    line=sline
    col=scol
    if DFS_limit(limit,int(0)):##受限DFS
        break

print(track)#1代表左，2代表下，3代表右，4代表上
time2=time.perf_counter()
print("运行时间： ",time2-time1)

##以下为可视化迷宫的代码
# 定义迷宫的大小和墙壁
maze = np.zeros((linenum, colnum))
for i in range(linenum):
    for j in range(colnum):
        if matrix[i][j]=='1':
            maze[i,j]=1    ##墙壁用黑色
# 定义起点和终点
start = (sline, scol)
end = (16, 1)##这里也可以两个for循环找得到
# 画迷宫图
fig, ax = plt.subplots()
ax.imshow(maze, cmap=plt.cm.binary)
ax.tick_params(axis='both', which='both', length=0)  ##隐藏刻度线
ax.plot(start[1], start[0], 'bo', markersize=7)  ##起点标记蓝色
ax.plot(end[1], end[0], 'ro', markersize=7)      ##终点标记红色
line=sline
col=scol
preline=sline
precol=scol
for i in range(len(track)):
    if (i==len(track)-1) or (track[i-1]!=track[i]):##变换方向或者达到终点的时候画线
        x=[precol,col]
        y=[preline,line]
        ax.plot(x,y,c='g',linewidth=3)
        preline=line
        precol=col
    if track[i]==1:
        col-=1
    elif track[i]==2:
        line+=1
    elif track[i]==3:
        col+=1
    else :
        line-=1
plt.show()
