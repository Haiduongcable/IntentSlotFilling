import numpy as np 
import cv2 
import time 
import json 
import os 


def load_coco(path_coco):
    '''
    Load coco annotation
    '''
    coco_annotation = json.load(open(path_coco, "r", encoding="utf-8"))
    human_annotation = coco_annotation["annotations"]