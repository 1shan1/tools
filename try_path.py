import os
from torch.utils.serialization import load_lua
import numpy as np
import pandas as pd

img_files='/home/pengshanzhen/try/data/split_train_label.txt'
pts_list = []
with open(img_files)as f:
  img_lines = f.readlines()
for img_line in img_lines:
  index = img_line.strip().rfind(' ')
  index1 = img_line.strip().rfind('/n')
  img_path = img_line[:index]
  anno_path = img_line[index+1:index1]
  #print(img_path)
  #print(anno_path)
  #exit()
  den = pd.read_csv(anno_path,sep=',',header=None).as_matrix()
  den  = den.astype(np.float32, copy=False)
  den = np.delete(den, -1, axis=1)  
  #l = den.shape[1]
  #den = den[][:-1]
  print(den)
  print(den.shape)
  exit()
  count = np.sum(den)
  
  if not os.path.isfile(img_path):
      continue
  if count == 0:
      continue
  
  pts_list.append([img_path, anno_path])



length = len(pts_list)
print(length)
