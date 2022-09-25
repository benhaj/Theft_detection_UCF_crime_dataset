from yacs.config import CfgNode

_C = CfgNode()

'''
The paths below should be modified to adapt your project

'''

############# 1. Model Paths #######################

## The pretrained model paths
_C.I3D_MODEL_PATH='/content/drive/Shareddrives/fiver/adib/pretrained_models/model_rgb.pth'
_C.C3D_MODEL_PATH='/content/drive/Shareddrives/fiver/adib/pretrained_models//C3D_Sport1M.pth'

_C.UCF_C3D_MODEL_PATH='/content/drive/Shareddrives/fiver/adib/pretrained_models/UCF_C3D_AUC_0.8143.pth'
## Vis Paths
_C.TEST_SPATIAL_ANNOTATION_PATH='/content/drive/Shareddrives/fiver/adib/data/Test_Spatial_Annotation.npy'
_C.TRAIN_SPATIAL_ANNOTATION_PATH='/content/drive/Shareddrives/fiver/adib/data/Train_Spatial_Annotation.npy'

############ 2. UCF Data ###########################

## THESE PATHS ARE CORRECT, BUT THE FILES STILL NEED TO BE FILTERED TO KEEP ONLY RELEVENT (THEFT)
_C.TRAIN_H5_PATH='/content/drive/Shareddrives/fiver/adib/data2/UCFCrime-Frames.h5'
_C.TEST_H5_PATH='/content/drive/Shareddrives/fiver/adib/data2/testing/UCFCrime-Frames-testing.h5'
_C.TESTING_TXT_PATH='/content/drive/Shareddrives/fiver/adib/data/Temporal_Anomaly_Annotation_New.txt'

_C.PSEUDO_LABEL_PATH_I3D='/content/drive/Shareddrives/fiver/adib/data/UCF_I3D_shoplifting_PLs.npy'
_C.PSEUDO_LABEL_PATH_C3D='/content/drive/Shareddrives/fiver/adib/data/UCF_C3D_shoplifting_PLs.npy'

############# 3. SHT Data ##########################
_C.SHT_TRAIN_H5_PATH='../data/SHT_Frames.h5'
_C.SHT_TEST_H5_PATH='../data/SHT_Frames.h5'

_C.SHT_TEST_MASK_DIR='../data/test_frame_mask/'
_C.SHT_TRAIN_TXT_PATH='../data/SH_Train_new.txt'
_C.SHT_TEST_TXT_PATH='../data/SH_Test_NEW.txt'

_C.PSEUDO_LABEL_PATH_SHT_I3D='../data/SHT_I3D_PLs.npy'
_C.PSEUDO_LABEL_PATH_SHT_C3D='../data/SHT_C3D_PLs.npy'

############# 4. Dataset Related ###################
_C.DATASET=CfgNode()
_C.DATASET.MEAN=[0.45,0.45,0.45]
_C.DATASET.STD=[0.225,0.225,0.225]

_C.DATASET.CROP_SIZE=224
_C.DATASET.RESIZE=256

_C.DATASET.C3D_MEAN=[90.25,97.66,101.41]
_C.DATASET.C3D_STD=[1,1,1]


############# 5.training setting ##################
_C.SEED=0
_C.LOG_DIR='/content/drive/Shareddrives/fiver/adib/logs/'
_C.SUMMARY_DIR='/content/drive/Shareddrives/fiver/adib/summarys/'
_C.MODEL_DIR='/content/drive/Shareddrives/fiver/adib/train_ckpts/'
_C.VIS_DIR='/content/drive/Shareddrives/fiver/adib/outputs/'

import os
def mkdir(path):
    if not os.path.exists(path):
        os.mkdir(path)

mkdir(_C.LOG_DIR)
mkdir(_C.SUMMARY_DIR)
mkdir(_C.MODEL_DIR)
mkdir(_C.VIS_DIR)
