import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()

x = np.linspace(0, 2*np.pi, 201)
ims = []
for i in range(100):
    y = np.sin(x + float(i)/50.0)
    im = plt.plot(x,y,'b')
    ims.append(im)

ani = animation.ArtistAnimation(fig, ims, interval=50)

# plt.show() # これを実行するとアニメーションが表示される。

ani.save('animation_test.gif', writer='imagemagick')
