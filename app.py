import re
from random import shuffle
from urllib.request import urlopen, Request
import tkinter as Tkinter
import click

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from mpl_toolkits.axes_grid1 import ImageGrid

input_file = "input/README.md"

grid_size = 20
regex1 = r'<!-- markdownlint-disable -->(.*)<!-- markdownlint-restore -->'
regex2 = r"<img src=\"(.*?)\" class=\"avatar-user\""

# input_file = 'README.md'

print(f"Getting contributors from {input_file}")
with open(input_file) as fp:
    r = fp.read()
    m1 = list(re.finditer(regex1, r, re.DOTALL))[0].group()
    m2 = re.finditer(regex2, r)
    all_contributors = [mm.groups()[0] for mm in m2]

fig = plt.figure(figsize=(4., 4.))
grid = ImageGrid(fig, 111,  # similar to subplot(111)
                nrows_ncols=(grid_size, grid_size),  # creates 2x2 grid of axes
                axes_pad=0.02,  # pad between axes in inch.
                share_all=True)

grid[0].get_yaxis().set_ticks([])
grid[0].get_xaxis().set_ticks([])

print("Plotting heart (this may take a while)")
for id, ax in enumerate(grid):
    y, x = grid_size / 2 - int(id / grid_size), - grid_size / 2 + int(id % grid_size)
    x /= (grid_size / 3)
    y /= (grid_size / 3)
    # print(f'x: {x} y: {y}')
    ax.axis('off')
    if (x ** 2 + y ** 2 - 1) ** 3 - (x ** 2) * (y ** 3) < 0 and all_contributors:
        shuffle(all_contributors)
        url = all_contributors.pop(0)
        if isinstance(url, str):
            req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            # Iterating over the grid returns the Axes.
            with urlopen(req) as f:
                img = Image.open(f)
                img = img.resize((64, 64))
                im = np.asarray(img)
        all_contributors.append(url)
        ax.imshow(im)

    else:
        # print('reject')
        pass


plt.box(False)
plt.axis('off')
plt.show()
