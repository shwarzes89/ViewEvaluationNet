import glob
import os
from py_utils import load_utils
import pickle


def getImagePath():
    image_path = './example_images'
    return os.path.join(image_path)

def get_test_list():
    image_list_path = './image_list.txt'
    image_path = './example_images'

    image_list = load_utils.load_string_list(image_list_path)
    image_path_list = []
    for s_image_name in image_list:
        s_full_image_path = os.path.join(image_path,s_image_name)
        if os.path.isfile(s_full_image_path):
            image_path_list.append(s_full_image_path)
    return image_path_list


def get_pdefined_anchors():
    pdefined_anchor_file_path = './datasets/pdefined_anchor.pkl'
    pdefined_file = open(pdefined_anchor_file_path, 'r')
    pdefined_anchors = pickle.load(pdefined_file)
    return pdefined_anchors
