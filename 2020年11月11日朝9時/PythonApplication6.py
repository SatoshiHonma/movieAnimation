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
with open(r'/Users/honmasatoshi/OneDrive - 東京理科大学/研究データ/2.5動画/CIMG0837.csv') as f:
    #print(f.read())
    reader = csv.reader(f)
    l=[row for row in reader]
    x=[]
    y=[]
    t=[]
    timestamp=[]
for i in range(1,1000):
    tempTimestanp=l[i][2]
    tempTimestanp=float(tempTimestanp)
    timestamp.append(tempTimestanp)
    xt=l[i][0]
    xt=float(xt)
    x.append(xt)
    yt=l[i][6]
    yt=float(yt)
    y.append(yt)
    t.append(i*10)
DELTA_T = 33.3 # アニメーション間隔[msec]
#FRAMES = t[-1] // DELTA_T # 必要な総フレーム数

pos = 0      # 描画時点の時間位置
def animate(i):
    # 描画時点の時間まで進める
    global pos
    while t[pos] < i*DELTA_T:
        pos += 1

    ax.cla()
    ax.set_xlim(pos-100, pos+100)
    ax.set_ylim(0, 50)

    #N_PLOT = 5 # 描画点の数
    # 描画時点からの時刻基準で未来方向の点群を描画してしまうけど、まあいいか…
    ax.plot( x[0:pos], y[0:pos],linestyle='solid',color="red",marker="o")

ani =animation.FuncAnimation(fig, animate, interval=33.3,repeat = True)
ani.save('ret.mp4', writer='ffmpeg')
#plt.show
