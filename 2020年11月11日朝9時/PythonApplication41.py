import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import csv

fig = plt.figure()
#x = np.arange(0, 10, 0.1)
with open(r'/Users/honmasatoshi/OneDrive - 東京理科大学/研究データ/2.5動画/CIMG0837.csv') as f:
    #print(f.read())
    reader = csv.reader(f)
    l=[row for row in reader]
    x=[]
    y=[]
for i in range(1,300):
    xt=l[i][0]
    xt=int(xt)
    x.append(xt)
    yt=l[i][6]
    yt=float(yt)
    y.append(yt)

#ims = [plt.plot(1,1,"ro"),plt.plot(2,2,"ro"),plt.plot(3,3,"ro"),plt.plot(4,4,"ro")]
ims = []
img=[]
x_lim = [0,100]
for i in range(1,300):

    x_lim[0]=i-50
    x_lim[1]=i+50
    #img = plt.plot(x[:i+1], y[:i+1], 'b-o')
    #if i+1-50 > 0:
    plt.xlim(x_lim[0],x_lim[1])
    plt.title("sample animation (real time)")
    img = plt.plot(x[i+1-50:i+1], y[i+1-50:i+1], 'ro')
        #plt.xlim(i-10, i+10)

    ims.append(img)
    #plt.xlim(i-10, i+10)

#print(type(l[1][1]))
ani = animation.ArtistAnimation(fig, ims, interval=10)
#ani.save('anim.gif', writer="imagemagick")
#ani.save('anim.mp4', writer="ffmpeg")
plt.show()

"""
for a in range(50):
    y = np.sin(x - a)
    line, = plt.plot(x, y, "r")
    ims.append([line])
"""
