import matplotlib.animation as animation
import matplotlib.pyplot as plt

ims = []
fig = plt.figure()
for i in range (1, 10):
    im = plt.scatter(i, i).findobj()
    ims.append(im)

ani = animation.ArtistAnimation(fig, ims, interval=200, repeat_delay=1000)

ani.save('test1.gif', writer='pillow')
