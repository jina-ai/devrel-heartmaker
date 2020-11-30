# Heart Maker

<p align="center">
  <a href="https://github.com/jina-ai/jina"><img align="center" src="example.png"></a>
</p>

This script:
- scrapes a list of contributor avatar URLs from a `README.md` file ([example](https://github.com/jina-ai/jina/#contributors-))
- creates a mosaic of the images in the shape of a heart
- presents the heart and allows user to save as image

## Usage

1. Ensure you've used [all-contributors](https://github.com/all-contributors/all-contributors) to get contributors into your repo's `README.md`
2. Clone this repo: 
3. `cd devrel-heartmaker`
4. Save your `README.md` into `input`
5. `pip install -r requirements.txt`
6. `python app.py`
7. The script will take a while (the more contributors, the more time)
8. A window will pop up allowing you to view and save the image

## FAQ

### The script can't see my contributors

Edit `regex1` and `regex2` in `app.py`

### How can I change the size of the avatars/heart?

Tweak `grid_size` in `app.py`

### Why are some avatars duplicated?

There are only a finite number of ways to fill a heart. You couldn't do it with just 1 or 2 avatars without duplication after all. As long as there are gaps in the heart, they have to be filled somehow, and we do this via duplication

### I have too many contributors, can't show them all

Change `grid_size = 20` to a larger number, say `grid_size = 30` (~ 150 contributors), `grid_size = 40` (~ 200 contributors) 

## Inspiration

- [code golf - Draw/plot a heart graph - Code Golf Stack Exchange](https://codegolf.stackexchange.com/questions/109917/draw-plot-a-heart-graph)
- [all-contributors/all-contributors: ✨ Recognize all contributors, not just the ones who push code ✨](https://github.com/all-contributors/all-contributors)
