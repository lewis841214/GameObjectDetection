import cv2 as cv
import matplotlib.pyplot as plt
import sys
import path
import glob

directory = path.Path(__file__).abspath()
print(directory.parent.parent)
sys.path.append(directory.parent.parent)

from utils import timeit

@timeit
def template_matching(template, target, meth = 'cv.TM_CCOEFF'):
    method = eval(meth)
    res = cv.matchTemplate(target,template, method)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    w, h = template.shape[::-1][-2:] # template.shape[::-1]
    bottom_right = (top_left[0] + w, top_left[1] + h)
    
    cv.rectangle(target,top_left, bottom_right, 255, 2)
    
    top_left_residule = 40
    bottom_right_residule = 160
    top_left = (top_left[0], top_left[1] + top_left_residule)
    bottom_right = (bottom_right[0], bottom_right[1] + bottom_right_residule)
    print(top_left, bottom_right)
    cv.rectangle(target,top_left, bottom_right, 255, 2)

    # plt.subplot(131),plt.imshow(res)
    # plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    # plt.subplot(132),plt.imshow(target)
    # plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    # plt.suptitle(meth)

    # plt.subplot(133),plt.imshow(template)
    # plt.title('template Point'), plt.xticks([]), plt.yticks([])
    # plt.show()

    plt.imshow(target)
    plt.show()

template = cv.imread('./data/objects/chracters/blue_blood/Screenshot from 2024-03-05 23-20-07.png' )#, cv.IMREAD_GRAYSCALE)

# target = cv.imread('./data/video_frames/1709649898.0186276.png')#, cv.IMREAD_GRAYSCALE)
methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
            'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']

# for meth in methods:
meth = 'cv.TM_CCOEFF'

all_targets = glob.glob('data/video_frames/*')
for tar_path in all_targets:
    target = cv.imread(tar_path)#, cv.IMREAD_GRAYSCALE)
    template_matching(template, target, meth)