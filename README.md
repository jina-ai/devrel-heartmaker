# Heart Maker

This script:
- scrapes a list of contributor avatar URLs from a `README.md` file ([example](https://github.com/jina-ai/jina/#contributors-))
- plots them into a heart shape
- presents the heart and allows user to save as image

<p align="center">
<img align="center" src="example.png">
</p>

## Usage

1. Ensure you've used [all-contributors](https://github.com/all-contributors/all-contributors) to get contributors into your repo's `README.md`
2. Save your `README.md` into `input`
3. `pip install -r requirements.txt`
4. `python app.py`
5. The script will take a while (the more contributors, the more time)
6. A window will pop up allowing you to view and save the image

## FAQ

### The script can't see my contributors

Edit `regex1` and `regex2` in `app.py`

### How can I change the size of the avatars/heart?

Tweak `grid_size` in `app.py`

### Why are some avatars duplicated?

There are only a finite number of ways to fill a heart. You couldn't do it with just 1 or 2 avatars without duplication after all. As long as there are gaps in the heart, they have to be filled somehow, and we do this via duplication

### Sources

- [code golf - Draw/plot a heart graph - Code Golf Stack Exchange](https://codegolf.stackexchange.com/questions/109917/draw-plot-a-heart-graph)
