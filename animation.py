"""
Gather all images from a folder and form an animation
input: dir with .png files
returns: a .gif file
"""

import os
import imageio


def animate_all_pngs(png_dir):
    """input directory for .png files"""

    images = []
    i = 0

    for subdir, dirs, files in os.walk(png_dir):
        imax = len(files)
        for file in files:

            file_path = os.path.join(subdir, file)
            if file_path.endswith(".png"):
                i += 1
                if i == 1:
                    images.append(imageio.imread(file_path))
                    images.append(imageio.imread(file_path))
                    images.append(imageio.imread(file_path))
                    images.append(imageio.imread(file_path))
                    images.append(imageio.imread(file_path))
                elif i == imax:
                    images.append(imageio.imread(file_path))
                    images.append(imageio.imread(file_path))
                    images.append(imageio.imread(file_path))
                    images.append(imageio.imread(file_path))
                    images.append(imageio.imread(file_path))
                else:
                    images.append(imageio.imread(file_path))

    imageio.mimsave(png_dir + 'movie.gif', images)
    print('gif wrote to {}'.format(png_dir))


if __name__ == '__main__':
    png_dir = "./hk_figs/"
    animate_all_pngs(png_dir)
