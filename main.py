# %%
from data_plotter import Plot
import matplotlib.animation as animation
import matplotlib.pyplot as plt


if __name__ == "__main__":
    fig = plt.figure()
    graph = Plot(fig)
    plot = graph.plot()
    plot.show()


# %%
