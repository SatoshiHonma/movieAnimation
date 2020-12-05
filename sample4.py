import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def update(frame):
    plt.cla()
    x = np.linspace(0, 2*np.pi, 201)
    y = np.sin(x + float(frame)/100.0)
    plt.plot(x,y,'b')

fig = plt.figure(figsize=(4,3), dpi=100)

ani = animation.FuncAnimation(fig, update, frames=range(0,2*314,10), interval=50)

#plt.show() # これを実行するとアニメーションが表示される。

w = animation.PillowWriter(fps=20)
ani.save('animation_test.gif', writer=w)
