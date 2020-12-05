import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import random



data_set = np.loadtxt(
    fname="sampleData.csv",
    dtype="float",
    delimiter=",",
)

#散布図を描画 → scatterを使用する
#1行ずつ取り出して描画
#plt.scatter(x座標の値, y座標の値)
#for data in data_set:
#    plt.scatter(data[1], data[2])

plt.title("SIN curve")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()


fig = plt.figure()
 
xlim = [0,100]
X, Y = [], []
 
def plot(data):
    plt.cla()                   # 前のグラフを削除
    
    for data in data_set:
        Y.append(data[2],)
        X.append(data[1],)
    
    if len(X) > 100:            # 描画範囲を更新
        xlim[0]+=1
        xlim[1]+=1
    
    plt.plot(X, Y)              # 次のグラフを作成
    plt.title("sample animation (real time)")
    plt.ylim(-1,2)
    plt.xlim(xlim[0],xlim[1])
    
 
# 10msごとにplot関数を呼び出してアニメーションを作成
ani = animation.FuncAnimation(fig, plot, interval=10, blit=True)
ani.save('sample2.gif', writer='imagemagick')
plt.show()
