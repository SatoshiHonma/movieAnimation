import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import time

# Simulated background data
x = np.linspace(0,61,62)
y = np.linspace(0,6,62)

# Set up the figure, the axis, and the plot element we want to animate
max_height = 6  # max height of y-axis
n_pts = 61      # max length of x-axis

# Original location for progress line
y1 = [0, max_height]
x1 = [0, 0]

fig = plt.figure()          # Initialize figure
#ax = fig.add_subplot(111)  # Intialize axes
ax = plt.axes(xlim=(0, n_pts), ylim=(0, max_height))    # Set axes limits
line, = ax.plot([], [], lw=2)                           # Initialize line

# draw the data to the 'background'
line1, = ax.plot(x, y, color='black')

# initialization function: plot the background of each frame
def init():
    line.set_data(x1, y1)
    return line,

starttime=time.time()
mytimer=0
mytimer_ref=0

# animation function.  This is called sequentially
def animate(i):
    t = time.time() - starttime
    mytimer = t + mytimer_ref
    x1 = [mytimer,mytimer]
    line.set_data(x1, y1)
    return line,

# call the animator.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=61, interval=1000)

# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html

writer = animation.writers['ffmpeg'](fps=1)

anim.save('demo.mp4')

plt.show()
