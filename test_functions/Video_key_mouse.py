import pyautogui
import time 
import pyscreeze
from utils import timeit
import cv2 as cv

video_frame_path = './data/video_frames'


@timeit
def get_screenshot():
    cur_time = time.time()
    im = pyautogui.screenshot(f'{video_frame_path}/{cur_time}.png')
    return im


while True:
    time.sleep(1)
    get_screenshot()
