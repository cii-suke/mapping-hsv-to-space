from PIL import Image
import numpy as np
from mappingHSV import MappingHSV
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def main():
    path = "./data/mandrill.jpg"
    img = np.array(Image.open(path))
    m = MappingHSV(img)
    d = m.mapping()
    plot_3d(d)


def plot_3d(X):
    fig = plt.figure(figsize=(5, 5))
    ax = fig.add_subplot(111, projection="3d")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_zlabel("Z-axis")
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_zlim(0, 1)

    ax.scatter(
        X[:, 0], X[:, 1], X[:, 2], linewidths=0.3, edgecolors="k", s=5, alpha=0.6
    )
    plt.show()


if __name__ == "__main__":
    main()
