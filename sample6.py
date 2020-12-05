import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig = plt.figure()
ax = fig.add_subplot(111)

def update(frame):
    ax.cla() # ax をクリア
    ax.plot(frame, 0, "o")

anim = FuncAnimation(fig, update, frames=range(8), interval=1000)

anim.save("c02.gif", writer="imagemagick")
plt.close()
