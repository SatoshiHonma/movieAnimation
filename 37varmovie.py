import wave
import numpy as np
import matplotlib.pyplot as plt
import csv
import pprint
from statistics import variance
from statistics import pvariance
import math
import matplotlib.animation as animation
import math
import csv


#CSVファイルを入力
with open("CIMG0837.csv") as csvfile:
    #reader = csv.reader(csvfile)
    #print(csvfile.read())
    reader = csv.reader(csvfile)
    l = [row for row in reader]
l[0].append("fvangleX")
l[0].append("fvangleY")
l[0].append("var_fvangleX")
l[0].append("var_fvangleY")
l[0].append("var_fvangle")

fvangleX=[]#turn
fvangleY=[]#updown
for i in range(1,len(l)-1):
    fvangleY.append((float(l[i+1][10])-float(l[i][10]))/(float(l[i+1][2])-float(l[i][2])))
    fvangleX.append((float(l[i+1][11])-float(l[i][11]))/(float(l[i+1][2])-float(l[i][2])))
    if fvangleX[-1]>0:
        fvangleX[-1]=0
    if fvangleY[-1]<0:
        fvangleY[-1]=0
    l[i].append(fvangleX[-1])
    l[i].append(fvangleY[-1])

var_fvangleX=[]
var_fvangleY=[]
var_fvangle=[]
for i in range(1,len(l)-11):
    b=[]
    c=[]
    for j in range(i,i+10):
        b.append(l[j][13])
        c.append(l[j][14])

    t_var_fvangleX=variance(b)
    t_var_fvangleY=variance(c)
    t_var_fvangle=t_var_fvangleY-t_var_fvangleX

    if t_var_fvangle<0:
        t_var_fvangle=0
    if t_var_fvangle>2000:
        t_var_fvangle=2000
    var_fvangleX.append(t_var_fvangleX)
    var_fvangleY.append(t_var_fvangleX)
    var_fvangle.append(t_var_fvangleX)
    l[i].append(t_var_fvangleX)
    l[i].append(t_var_fvangleY)
    l[i].append(t_var_fvangle)

with open("3_with_var.csv", 'w') as f:
    writer = csv.writer(f)
    writer.writerows(l)

graphX=[]
graphY=[]
for i in range(1,len(l)-11):
    graphX.append(l[i][0])
    graphY.append(l[i][-1])

fig, ax = plt.subplots()

# 前処理としてデータ読込と
# 時間を先頭からの累積経過時間に変換する処理が必要
"""
# テストデータの生成
x,y,t = [],[],[]
for i in range(1000):
    t.append(i*10) # 先頭からの累積経過時間[msec]

    # 適当な周回運動
    x.append(math.cos(i/25.0)*10)
    y.append(math.sin(i/25.0)*10)

with open(r'/Users/honmasatoshi/OneDrive - 東京理科大学/研究データ/2.5動画/CIMG0841.csv') as f:
    #print(f.read())
    reader = csv.reader(f)
    l=[row for row in reader]
    x=[]
    y=[]
    t=[]
    timestamp=[]
    #print(len(l))
#for i in range(1,9000):
"""
x=[]
y=[]
t=[]
timestamp=[]

for i in range(1,len(l)-11):
    tempTimestanp=l[i][2]
    #tempTimestanp=float(tempTimestanp)
    timestamp.append(tempTimestanp)
    xt=l[i][0]
    xt=float(xt)
    x.append(xt)
    yt=l[i][-1]
    yt=float(yt)
    y.append(yt)
    t.append(i)

DELTA_T = 33.3 # アニメーション間隔[msec]
#FRAMES = t[-1] // DELTA_T # 必要な総フレーム数
#print(x)
'''
print('len(x)'+str(len(x)))
print('x[-1]'+str(x[-1]))
print('len(y)'+str(len(y)))
print('len(t)'+str(len(t)))
print('len(timestamp)'+str(len(timestamp)))
print('len(range(1,500))'+str(len(range(1,500))))
print('len(l)'+str(len(l)))
print('range(0,len(l))'+str(range(0,len(l))))
'''


pos = 0      # 描画時点の時間位置
def animate(k):
    # 描画時点の時間まで進める
    #global pos
    #while t[pos] < i:#*DELTA_T:
    #    pos += 1

    ax.cla()
    ax.set_xlim(k-100, k+100)
    ax.set_ylim(0, 2000)

    #N_PLOT = 5 # 描画点の数
    # 描画時点からの時刻基準で未来方向の点群を描画してしまうけど、まあいいか…
    if k<300:
        ax.plot( x[0:k], y[0:k],linestyle='solid',color="red",marker="o")
    if k>=300:
        ax.plot( x[k-300:k], y[k-300:k],linestyle='solid',color="red",marker="o")
    #ax.plot( x[0:k], y[0:k],linestyle='solid',color="red",marker="o")
    plt.title("var_fvangle(CIMG0837)"+timestamp[k])
#ani =animation.FuncAnimation(fig, animate, frames=range(0,8999),interval=33.3,repeat = True,blit=True)
ani =animation.FuncAnimation(fig, animate, frames=range(0,len(l)-11),interval=33.3,repeat = True)
ani.save('var_fvangle(CIMG0837).mp4', writer='ffmpeg')
#plt.show


'''

pos = 0      # 描画時点の時間位置
def animate(i):
    # 描画時点の時間まで進める
    global pos
    while t[pos] < i:#*DELTA_T:
        pos += 1

    ax.cla()
    ax.set_xlim(pos-100, pos+100)
    ax.set_ylim(0, 50)

    #N_PLOT = 5 # 描画点の数
    # 描画時点からの時刻基準で未来方向の点群を描画してしまうけど、まあいいか…
    ax.plot( x[0:pos], y[0:pos],linestyle='solid',color="red",marker="o")

ani =animation.FuncAnimation(fig, animate, interval=33.3,repeat = True)
ani.save('dougaa.mp4', writer='ffmpeg')
#plt.show
'''


'''
print(graphX)
print(graphY)
plt.plot(graphX, graphY)
plt.show()
'''
