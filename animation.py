"""
Gather all images from a folder and form an animation
input: dir with .png files
returns: a .gif file
"""

import os
import imageio

# input
png_dir = "./hk_figs/"

images = []

# TODO
# Read data according to months (1 then 2 not 11)

for subdir, dirs, files in os.walk(png_dir):
    for file in files:
        file_path = os.path.join(subdir, file)
        if file_path.endswith(".png"):
            images.append(imageio.imread(file_path))

imageio.mimsave('./hk_figs/movie.gif', images)