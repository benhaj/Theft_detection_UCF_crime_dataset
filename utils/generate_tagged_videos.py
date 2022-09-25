#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import argparse
import glob
import cv2
import numpy as np

parser = argparse.ArgumentParser(description='A program that uses the generated output images (feature maps) to generated tagged videos')
parser.add_argument("--inputdir", help="Write down the directory where the videos are")
parser.add_argument("--featuremaps", help="Write down the path where you stored the feature maps", default='/outputs/' )
parser.add_argument("--tagged_videos_dir", help="Write down the path/directory where you want to store the tagged videos")

if __name__=='__main__':
    args = vars(parser.parse_args())
    if not all(args.values()):
        parser.error('No arguments provided.')
    else:
      args = parser.parse_args()
      input_videos_dir = args.inputdir
      outputs_dir = args.featuremaps
      tagged_videos_dir = args.tagged_videos_dir

      elems = glob.glob(outputs_dir+"*.jpg")
      listed = [elem.split('/')[-1] for elem in elems]
      d = {}
      for x in listed:
        key = x.split('-')[0]+'.mp4'
        if key not in d.keys():
          d[key]=[]
        frame_value = x.split('-')[1]
        proba_ = round(float(x.split('-')[2][:-4]),3)
        d[key].append([frame_value,proba_])

      ### HERE PUT THE PATH OF THE VIDEOS THAT WERE TESTED
      elems = glob.glob(input_videos_dir+'*.mp4')                        
      
      for video_path in elems:
        cap = cv2.VideoCapture(video_path)
        cap.set(cv2.CAP_PROP_FPS, 30)
        length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        video_name = video_path.split('/')[-1]
        frames_indexes = [int(k[0]) for k in d[video_name]]
        sorted_frames_indexes = sorted(frames_indexes)
        probabilities = [float(k[1]) for k in d[video_name]]
        sorted_probabilities = np.array(probabilities)[np.argsort(frames_indexes)]

        if len(frames_indexes)!=0 :
          fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
          output = cv2.VideoWriter(tagged_videos_dir+video_name.split(".")[0]+"_tagged.mp4",fourcc, 20.0,     (int(cap.get(3)),int(cap.get(4))), 1)
          i=0
          while(i<length):
              
            # type of font to be used.
            font = cv2.FONT_HERSHEY_SIMPLEX

            # Capture frames in the video
            ret, frame = cap.read()

            ## if index in the model's output indexes (frame indexes where the model captured shoplifting)
            if i in range(min(frames_indexes),max(frames_indexes)):
              if i in sorted_frames_indexes:
                proba_ = sorted_probabilities[sorted_frames_indexes.index(i)]
              
              # Use putText() method for inserting text on video
              cv2.putText(frame, 
                          f'SHOPLIFTING {proba_}', 
                          (20, int(cap.get(4))-50), 
                          font, 0.7, 
                          (0, 0, 255), 
                          3)
                  
            output.write(frame)
            i = i +1
          print(20*'=')
          print(f'{video_path.split(".")[0]+"tagged"}.mp4')
          print('Done!')
          cap.release()
          output.release()

      
      

