# import re
from random import shuffle, seed
from urllib.request import urlopen, Request

# import tkinter as Tkinter
import click

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from mpl_toolkits.axes_grid1 import ImageGrid

# import requests
import os
from github import Github
from dotenv import load_dotenv

# Load token from .env file
load_dotenv()
token = os.environ["GITHUB_TOKEN"]

# Important settings
grid_size = 30  #       Higher = more squares in heart
avatar_size = 20  #     Higher = bigger squares in heart
dpi = 300  #            Higher = higher res output image


def get_contributors(org, token):
    g = Github(token)
    org = g.get_organization(org)

    repos = []
    # contrib_counter = 0

    # Get repos
    all_repos = org.get_repos()

    for repo in all_repos:
        repos.append(str(repo.full_name))

    # Get contributors
    print(f"Getting contributors from {org.name}'s {len(repos)} repositories")

    all_contributors = []
    for repo in repos:
        repo = g.get_repo(repo)
        contribs = repo.get_contributors()
        for user in contribs:
            if not user.avatar_url in all_contributors:
                all_contributors.append(user.avatar_url)

    all_contributors = set(all_contributors)  # Ensure no duplicates
    all_contributors = list(all_contributors)  # Ensure no duplicates

    print(f"Total {len(all_contributors)} contributors")

    return all_contributors


@click.command()
@click.option("--org", help="Name of your GitHub organization", required=True)
@click.option(
    "--token", help="GitHub token", default=os.environ["GITHUB_TOKEN"], required=True
)
def make_heart(org, token):
    all_contributors = get_contributors(org, token)
    cells_in_heart = 0

    fig = plt.figure(figsize=(4.0, 4.0))
    grid = ImageGrid(
        fig=fig,
        rect=111,  # similar to subplot(111)
        nrows_ncols=(grid_size, grid_size),  # creates 2x2 grid of axes
        axes_pad=0.02,  # pad between axes in inch.
        share_all=True,
    )

    grid[0].get_yaxis().set_ticks([])
    grid[0].get_xaxis().set_ticks([])

    contribs_in_grid = []
    # contribs_not_in_grid = all_contributors # No users are in the grid to begin with
    # squares_in_grid = 0

    print("Plotting heart (this may take a while)")
    for id, ax in enumerate(grid):
        # print(f"\t- Filling grid square {id}")
        y, x = grid_size / 2 - int(id / grid_size), -grid_size / 2 + int(id % grid_size)
        x /= grid_size / 3
        y /= grid_size / 3
        ax.axis("off")
        if (x ** 2 + y ** 2 - 1) ** 3 - (x ** 2) * (y ** 3) < 0 and all_contributors:
            cells_in_heart += 1
            # squares_in_grid += 1 # Track total squares
            # seed(random_seed)
            # shuffle(all_contributors)
            url = all_contributors.pop(0)
            # contribs_not_in_grid.remove(url)
            if (
                url not in contribs_in_grid
            ):  # and if heart not complete yet # If user is not in the heart
                contribs_in_grid.append(url)  # Track if user in grid or not
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

    # contribs_not_in_grid = list(set(all_contributors) - set(contribs_in_grid))
    contribs_in_grid = list(set(contribs_in_grid))  # deduplicate
    print(f"{len(contribs_in_grid)}/{len(all_contributors)} were added to the heart. Total cells: {cells_in_heart}")

    # print(f"Heart has {squares_in_grid} squares")
    # print(f"{len(contribs_in_grid)} users NOT in heart")
    # for url in contribs_not_in_grid:
    # username = url.split("/")[-1] # strip off url string
    # username = username[:-4] # strip off .png
    # print(f"- {username}")

    plt.box(False)
    plt.axis("off")
    # plt.show()

    # Render heart end

    # Save image
    plt.savefig(
        "heart.png", transparent=True, bbox_inches="tight", pad_inches=0, dpi=dpi
    )


if __name__ == "__main__":
    make_heart()
