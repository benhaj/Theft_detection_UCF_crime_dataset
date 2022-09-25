# !/usr/bin/env python
# coding: utf-8

import cv2
import h5py
import os
from tqdm import tqdm
import numpy as np
import argparse
import glob

"""
For training speed, we translate the video datasets into a single h5py file for reducing the indexing time in Disk
By keeping the compressed type as JPG, we can reduce the memory space
Here, we give the example as translating UCF-Crime training set into a single h5py file, you can modify it for other dataset
"""


def Video2ImgH5(video_dir,h5_path,train_list,segment_len=16,max_vid_len=2000):
    # not multi-thread, may take time
    h=h5py.File(h5_path,'a')
    for path in tqdm(train_list):
        vc=cv2.VideoCapture(os.path.join(video_dir,path))
        vid_len=vc.get(cv2.CAP_PROP_FRAME_COUNT)
        for i in tqdm(range(int(vid_len//segment_len))):
            tmp_frames=[]
            key=path.split('/')[-1].split('.')[0]+'-{0:06d}'.format(i)
            for j in range(segment_len):
                ret,frame=vc.read()
                _,frame=cv2.imencode('.JPEG',frame)
                frame=np.array(frame).tostring()
                if ret:
                    tmp_frames.append(frame)
                else:
                    print('Bug Reported!')
                    exit(-1)
            tmp_frames = np.asarray(tmp_frames)
            h.create_dataset(key,data=tmp_frames,chunks=True)
        print(path)

    print('finished!')

parser = argparse.ArgumentParser(description='A program that takes input directory containing videos, and output a .h5 file.')
parser.add_argument("--inputdir", help="Write down the directory where the videos are")
parser.add_argument("--outputdir", help="Write down the path where you want to store the .h5 file")


if __name__=='__main__':
    args = parser.parse_args()
    video_dir = args.inputdir
    h5_file_path = args.outputdir
    elems = glob.glob(f"{video_dir}/*.mp4")
    listed = [elem.split('/')[-1] for elem in elems]
    Video2ImgH5(video_dir,h5_file_path,listed,segment_len=16)





