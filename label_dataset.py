# label_dataset
# label images in different classes after unzipping the dataset
# Author: Yangjia Li (Francis)
# Date: Apr. 06, 2021
# Last_Modified: Apr. 25, 2021

import cv2
import pandas as pd
from pathlib import Path
from tqdm import tqdm

# TODO: download and unzip images
# path to the dataset
dataset_path = Path(r'C:\Users\franc\Documents\Dataset\real_face_mask')
mask_path = dataset_path/'with_mask'
nomask_path = dataset_path/'without_mask'

mask_dataframe = pd.DataFrame()

# iterate over folders and subfolders in nomask and mask dataset.
# label nomask images with '0' and mask images with '1'
for img_folder in tqdm(list(mask_path.iterdir()), desc='mask photos'):
    for img_path in img_folder.iterdir():
        maskDF = maskDF.append({
            'image': str(img_path),
            'mask_label': 1
        }, ignore_index=True)

for img_folder in tqdm(list(nomask_path.iterdir()), desc='non mask photos'):
    for imgPath in img_folder.iterdir():
        maskDF = maskDF.append({
            'image': str(img_path),
            'mask_label': 0
        }, ignore_index=True)

# store as 'serialized dataset'
# pickling => convert an object hierarchy into a byte stream
dataframe_name = 'C:/Users/franc/Documents/Dataset/maskdata.pkl'
print(f'saving Dataframe to: {dataframe_name)}')
mask_dataframe.to_pickle('dataframe_name')