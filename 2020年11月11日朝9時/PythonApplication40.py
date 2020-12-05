import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.animation import ArtistAnimation

fig, ax = plt.subplots()
ax.set_xlim(2018, 2020)
ax.set_ylim(0, 500)

artists = []
for index, value in enumerate([2019, 2020]):
    if index % 2 == 0:
        years = [2018, 2019]
        year_money = [100, 300]
    else:
        years = [2018, 2019, 2020]
        year_money = [100, 300, 200]
    plt.gca().get_xaxis().set_major_locator(ticker.MaxNLocator(integer=True))  # Xを整数で表示
    artists.append(ax.plot(years, year_money, lw=5))

animation = ArtistAnimation(fig, artists, interval=500, repeat_delay=1000)

plt.show()
