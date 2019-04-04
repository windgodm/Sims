import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, BoundaryNorm


def update_map(lifes_map):

    s = lifes_map.shape
    w = s[1]
    d = s[0]
    temp = np.zeros((d, w), dtype=np.int8)

    for y in range(d):
        for x in range(w):
            if lifes_map[y, x] == 1:  # (int8{1} is 1)(false) (int8{1} == 1)(True)
                around_cells = ([y - 1, x - 1], [y - 1, x], [y - 1, x + 1],
                                [y, x - 1], [y, x + 1],
                                [y + 1, x - 1], [y + 1, x], [y + 1, x + 1])

                for position in around_cells:
                    y1 = position[0]
                    x1 = position[1]
                    if 0 <= y1 < d and 0 <= x1 < w:
                        temp[y1, x1] += 1

    for y in range(d):
        for x in range(w):
            if temp[y, x] == 3:  # birth
                lifes_map[y, x] = 1
            elif temp[y, x] != 2:  # died
                lifes_map[y, x] = 0

    return lifes_map


def main():
    # version
    print("version: game of life v0")
    print("date: ?")

    # color map and norm
    colors = [(0, 0, 0), (0, 1, 0)]  # (r, g, b) [black, green]
    bounds = [0, 1, 2]
    cm = ListedColormap(colors)
    no = BoundaryNorm(bounds, cm.N)

    # fig
    fig, ax = plt.subplots()

    # data
    while True:
        size = int(input("map size>"))
        map_height = size.shape[0]
        map_width = size.shaoe[1]
        lifes_map = np.zeros((map_height, map_width), dtype=np.int8)

        # input
        while True:
            s = input("position>")
            s = s.split(" ")
            if s[0] is 'e':
                break

            pass  # check input 1.int 2.limit
            x = int(s[0])
            y = int(s[1])
            lifes_map[map_height-y-1, x] = 1
            plt.imshow(lifes_map, cmap=cm, norm=no)
            plt.pause(0.1)

        # sim
        while True:
            s = input("go on>")
            lifes_map = update_map(lifes_map)
            plt.imshow(lifes_map, cmap=cm, norm=no)
            plt.pause(0.1)


if __name__ == '__main__':
    main()
