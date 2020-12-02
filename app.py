import re
from random import shuffle
from urllib.request import urlopen, Request
import tkinter as Tkinter
import click

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from mpl_toolkits.axes_grid1 import ImageGrid
import requests
import os
from github import Github

# Key settings
grid_size = 20
avatar_size = 64

# Get Contributors start

@click.command()
@click.option("--org", help="Name of your GitHub organization", required=True)
@click.option(
    "--token", help="GitHub token", default=os.environ["GITHUB_TOKEN"], required=True
)
def make_heart(org, token):
    g = Github(token)
    org = g.get_organization(org)

    repos = []
    contrib_counter = 0

    all_repos = org.get_repos()

    for repo in all_repos:
        repos.append(str(repo.full_name))

    print(f"Getting contributors from {org.name}'s {len(repos)} repositories")

    all_contributors = []
    for repo in repos:
        repo = g.get_repo(repo)
        contribs = repo.get_contributors()
        for user in contribs:
            if not user.avatar_url in all_contributors:
                all_contributors.append(user.avatar_url)
    # Get Contributors end

    # Render heart start
    fig = plt.figure(figsize=(4.0, 4.0))
    grid = ImageGrid(
        fig,
        111,  # similar to subplot(111)
        nrows_ncols=(grid_size, grid_size),  # creates 2x2 grid of axes
        axes_pad=0.02,  # pad between axes in inch.
        share_all=True,
    )

    grid[0].get_yaxis().set_ticks([])
    grid[0].get_xaxis().set_ticks([])

    print("Plotting heart (this may take a while)")
    for id, ax in enumerate(grid):
        y, x = grid_size / 2 - int(id / grid_size), -grid_size / 2 + int(id % grid_size)
        x /= grid_size / 3
        y /= grid_size / 3
        ax.axis("off")
        if (x ** 2 + y ** 2 - 1) ** 3 - (x ** 2) * (y ** 3) < 0 and all_contributors:
            shuffle(all_contributors)
            url = all_contributors.pop(0)
            if isinstance(url, str):
                req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
                # Iterating over the grid returns the Axes.
                with urlopen(req) as f:
                    img = Image.open(f)
                    img = img.resize((avatar_size, avatar_size))
                    im = np.asarray(img)
            all_contributors.append(url)
            ax.imshow(im)

        else:
            pass

    plt.box(False)
    plt.axis("off")
    plt.show()

    # Render heart end


if __name__ == "__main__":
    make_heart()
