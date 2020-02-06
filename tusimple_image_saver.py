import cv2
import numpy as np
import json
import os
from argparse import ArgumentParser as ArgParse

def process(json_file):
  path = '/home/nikhil/Documents/task/lanenet-expo/all-in-one'
  with open(json_file, 'r') as file:
    json_lines = file.readlines()
    for i in json_lines:
      sample = json.loads(i)
      lanes = sample['lanes']
      raw_file = sample['raw_file']
      y_samples = sample['h_samples']
      # if os.path.exists(raw_file):
      #   continue
      # else:
        
      img = cv2.imread(raw_file)
      if img is None:
        continue
      else:        

        # img = cv2.imread(raw_file)
        image_name = raw_file.split('/')[-1]
        img_path = os.path.join(path, image_name)
        print("images are saved in : {}".format(img_path))
        
        pred_lanes_vis = [[(x, y) for (x, y) in zip(lane, y_samples) if x >= 0] for lane in lanes]
        img_vis = img.copy()
        
        for lane in pred_lanes_vis:
          cv2.polylines(img_vis, np.int32([lane]), isClosed=False, color=(238,238,175), thickness=3)
          cv2.imwrite(img_path, img_vis)

if __name__=='__main__':
  ap = ArgParse()
  ap.add_argument('--json_file', type=str, default='Predction or annotation json file')
  args = ap.parse_args()
  process(args.json_file)