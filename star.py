from matplotlib import pyplot as plt
from skimage.feature import blob_log
from math import sqrt
from matplotlib import cm
import glob
from skimage.color import rgb2gray
from skimage.io import imread

example_file = glob.glob("star.jpg")[0]
im = imread(example_file)
im_gray = rgb2gray(im)

plt.imshow(im_gray, cmap=cm.gray)
plt.show()

blobs_log = blob_log(im_gray, max_sigma=100, num_sigma=5, threshold=.1)
blobs_log[:, 2] = blobs_log[:, 2] * sqrt(2)

numrows = len(blobs_log)
print("Number of stars counted:", numrows)

fig, ax = plt.subplots(1, 1)
plt.imshow(im_gray, cmap=cm.gray)

for blob in blobs_log:
    y, x, r = blob
    c = plt.Circle((x, y), r+5, color='lime', linewidth=2, fill=False)
    ax.add_patch(c)

plt.show()
