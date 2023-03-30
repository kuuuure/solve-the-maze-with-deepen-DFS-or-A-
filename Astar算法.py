#请将附件放在桌面并且更改下方路径的用户名
#下面两个库可以将这个迷宫可视化
import matplotlib.pyplot as plt
import numpy as np
import math
import time
time1=time.perf_counter()
matrix=[]#迷宫矩阵
linenum=18
colnum=36
track=[]
sline=int(0)##起点坐标
scol=int(0)
eline=int(0)##终点坐标
ecol=int(0)


def addtrack(l,c,fl,fc):
    global track
    if fc==c+1:
        track.append(int(1))
    elif fl==l-1:
        track.append(int(2))
    elif fc==c-1:
        track.append(int(3))
    elif fl==l+1:
        track.append(int(4))

##A星算法，h(x)设为欧式距离
def Astar():
    global track,linenum,colnum,sline,scol,eline,ecol
    open=[]     ##两个列表
    closed=[]
    f0=math.sqrt((eline-sline)*(eline-sline)+(ecol-scol)*(ecol-scol))
    open.append([sline,scol,0,f0,f0,-1,-1]) ##4个参数，坐标，g（n）,h(n),父节点坐标
    finish=bool(False)
    while len(open)!=0 :
        line=open[0][0]
        col=open[0][1]
        f=open[0][2]

        if matrix[line][col]=='E':       ##得到终点以后
            fline=open[0][5]
            fcol=open[0][6]
            while matrix[line][col]!='S':
                for i in range(len(closed)):
                    if closed[i][0]==fline and closed[i][1]==fcol:
                        addtrack(line,col,fline,fcol)
                        line=fline
                        col=fcol
                        fline=closed[i][5]
                        fcol=closed[i][6]
                        closed.pop(i)
                        break
            track.reverse()
            return

        closed.insert(0,open[0])
        open.pop(0)
        sonlist=[[line,col-1],[line+1,col],[line,col+1],[line-1,col]]
        for i in range(len(sonlist)):
            if sonlist[i][0] >=0 and sonlist[i][0] < linenum and sonlist[i][1] >=0 and sonlist[i][1] <= colnum and matrix[sonlist[i][0]][sonlist[i][1]]!='1':
                h=math.sqrt((eline-sonlist[i][0])*(eline-sonlist[i][0])+(ecol-sonlist[i][1])*(ecol-sonlist[i][1]))
                f=closed[0][2]+1+h
                e=bool(False)   ##判断是否已经加入了
                for j in range(len(open)):
                    if open[j][0]==sonlist[i][0] and open[j][1]==sonlist[i][1]:
                        e=bool(True)
                        if f<open[j][4]:
                            open.pop(j)
                            for k in range(len(open)+1):
                                if k==len(open):
                                    open.append([sonlist[i][0],sonlist[i][1],closed[0][2]+1,h,f,line,col])
                                    break
                                if open[k][4]>=f:
                                    open.insert(k,[sonlist[i][0],sonlist[i][1],closed[0][2]+1,h,f,line,col])
                                    break
                        break
                if e:
                    continue
                for j in range(len(closed)):
                    if closed[j][0]==sonlist[i][0] and closed[j][1]==sonlist[i][1]:
                        e=bool(True)
                        if f<closed[j][4]:
                            closed.pop(j)
                            for k in range(len(open)+1):
                                if k==len(open):
                                    open.append([sonlist[i][0],sonlist[i][1],closed[0][2]+1,h,f,line,col])
                                    break
                                if open[k][4]>=f:
                                    open.insert(k,[sonlist[i][0],sonlist[i][1],closed[0][2]+1,h,f,line,col])
                                    break
                        break

                if e:
                    continue

                for k in range(len(open)+1):
                    if k==len(open):
                        open.append([sonlist[i][0], sonlist[i][1], closed[0][2] + 1, h, f, line, col])
                        break
                    if open[k][4]>=f:
                        open.insert(k, [sonlist[i][0], sonlist[i][1], closed[0][2] + 1, h, f, line, col])
                        break


##main 函数
s=[]
f=open("C:\\Users\\LHH\\Desktop\\MazeData.txt")    ##文件路径
for i in range(18):
    st=f.readline()
    s=[]
    for j in range(36):
        s.append(st[j])
    matrix.append(s)
for i in range(18):
    for j in range(36):
        if matrix[i][j] == 'S':
            sline = i
            scol = j
        if matrix[i][j] == 'E':
            eline = i
            ecol = j
##得到起点坐标 (sline,scol),终点坐标（eline,ecol）
Astar()
print(track)
time2=time.perf_counter()
print("运行时间： ",time2-time1)

# 定义迷宫的大小和墙壁
maze = np.zeros((linenum, colnum))
for i in range(linenum):
    for j in range(colnum):
        if matrix[i][j]=='1':
            maze[i,j]=1    ##墙壁用黑色

# 定义起点和终点
start = (sline, scol)
end = (eline, ecol)

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
