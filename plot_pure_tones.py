"""Create figures to illustrate multiple pure tones.


"""
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb


if __name__ == '__main__':

    from matplotlib import rcParams as defaults

    figsize = defaults["figure.figsize"]
    defaults["figure.figsize"] = [figsize[0], int(figsize[1] / 2)]
    defaults["lines.linewidth"] = 2
    defaults["font.size"] = 14

    x = np.linspace(0, 40 * np.pi, 44100)
    x_longer = np.linspace(0, 5 * np.pi, int(44100 / 8))

    tones = (
        np.sin(x),
        np.sin(np.concatenate((x, x_longer))),
        np.sin(2.1 * x),
        np.sin(x + np.pi/2),
        2.1 * np.sin(x)
    )

    for i, tone in enumerate(tones):

        fig, ax = plt.subplots(1, 1, constrained_layout=True)
        ax.plot(tones[i], f"C{i}")
        if i > 0: ax.plot(tones[0], ls="--")
        ax.set_xticks([], [])
        ax.set_yticks([], [])
        ax.set_xlim(0, len(tones[i]))
        ax.set_ylim(tones[i].min(), tones[i].max())
        ax.set_xlabel("Time")
        ax.set_ylabel("Pressure")
        sb.despine(fig, ax, top=True, right=True)
        plt.savefig(f"pure_tones_{i}.svg", bbox_inches=0, transparent=True)

