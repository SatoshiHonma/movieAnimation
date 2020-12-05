import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math
import numpy as np
import csv

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
"""
with open(r'/Users/honmasatoshi/OneDrive - 東京理科大学/研究データ/本間実験依頼/頷きアンケート整理/CIMG0840anke.csv') as f:
    #print(f.read())
    reader = csv.reader(f)
    l=[row for row in reader]
    x=[]
    ya=[]
    yb=[]
    yc=[]
    yd=[]
    ye=[]
    t=[]
    timestamp=[]
    #print(len(l))
#for i in range(1,9000):
for i in range(1,len(l)-1):
    tempTimestanp=l[i][1]
    #tempTimestanp=float(tempTimestanp)
    timestamp.append(tempTimestanp)
    xt=l[i][0]
    xt=float(xt)
    x.append(xt)

    ya_t=l[i][2]
    ya_t=float(ya_t)
    ya.append(ya_t)

    yb_t=l[i][3]
    yb_t=float(yb_t)
    yb.append(yb_t)

    yc_t=l[i][4]
    yc_t=float(yc_t)
    yc.append(yc_t)


DELTA_T = 33.3 # アニメーション間隔[msec]
#FRAMES = t[-1] // DELTA_T # 必要な総フレーム数
#print(x)


def animate(k): #1
    # 描画時点の時間まで進める
    #global pos
    #while t[pos] < i:#*DELTA_T:
    #    pos += 1

    ax.cla()
    ax.set_xlim(k-10, k+5)
    ax.set_ylim(0, 3)

    #N_PLOT = 5 # 描画点の数
    # 描画時点からの時刻基準で未来方向の点群を描画してしまうけど、まあいいか…
    if k<300:
        ax.plot( x[0:k], ya[0:k],linestyle='solid',color="red",marker="o")
    if k>=300:
        ax.plot( x[k-300:k], ya[k-300:k],linestyle='solid',color="red",marker="o")
    #ax.plot( x[0:k], y[0:k],linestyle='solid',color="red",marker="o")
    goukei = 0
    for p in range(1,k):
        goukei += int(ya[p])
    plt.title("anke(CIMG0840)honma"+timestamp[k]+"total"+str(goukei))
#ani =animation.FuncAnimation(fig, animate, frames=range(0,8999),interval=33.3,repeat = True,blit=True)
ani =animation.FuncAnimation(fig, animate, frames=range(0,len(l)-2),interval=1000,repeat = True)
ani.save('anke(CIMG0840)honma.mp4', writer='ffmpeg')
#plt.show


def animate(k): #2
    # 描画時点の時間まで進める
    #global pos
    #while t[pos] < i:#*DELTA_T:
    #    pos += 1

    ax.cla()
    ax.set_xlim(k-10, k+5)
    ax.set_ylim(0, 3)

    #N_PLOT = 5 # 描画点の数
    # 描画時点からの時刻基準で未来方向の点群を描画してしまうけど、まあいいか…
    if k<300:
        ax.plot( x[0:k], yb[0:k],linestyle='solid',color="red",marker="o")
    if k>=300:
        ax.plot( x[k-300:k], yb[k-300:k],linestyle='solid',color="red",marker="o")
    #ax.plot( x[0:k], y[0:k],linestyle='solid',color="red",marker="o")
    goukei = 0
    for p in range(1,k):
        goukei += int(yb[p])
    plt.title("anke(CIMG0840)huruhata"+timestamp[k]+"total"+str(goukei))
#ani =animation.FuncAnimation(fig, animate, frames=range(0,8999),interval=33.3,repeat = True,blit=True)
ani =animation.FuncAnimation(fig, animate, frames=range(0,len(l)-2),interval=1000,repeat = True)
ani.save('anke(CIMG0840)huruhata.mp4', writer='ffmpeg')
#plt.show


def animate(k): #3
    # 描画時点の時間まで進める
    #global pos
    #while t[pos] < i:#*DELTA_T:
    #    pos += 1

    ax.cla()
    ax.set_xlim(k-10, k+5)
    ax.set_ylim(0, 3)

    #N_PLOT = 5 # 描画点の数
    # 描画時点からの時刻基準で未来方向の点群を描画してしまうけど、まあいいか…
    if k<300:
        ax.plot( x[0:k], yc[0:k],linestyle='solid',color="red",marker="o")
    if k>=300:
        ax.plot( x[k-300:k], yc[k-300:k],linestyle='solid',color="red",marker="o")
    #ax.plot( x[0:k], y[0:k],linestyle='solid',color="red",marker="o")
    goukei = 0
    for p in range(1,k):
        goukei += int(yc[p])
    plt.title("anke(CIMG0840)tanizaki"+timestamp[k]+"total"+str(goukei))
#ani =animation.FuncAnimation(fig, animate, frames=range(0,8999),interval=33.3,repeat = True,blit=True)
ani =animation.FuncAnimation(fig, animate, frames=range(0,len(l)-2),interval=1000,repeat = True)
ani.save('anke(CIMG0840)tanizaki.mp4', writer='ffmpeg')
#plt.show
