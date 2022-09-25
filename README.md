# Theft_detection_UCF_crime_dataset

This project is mainly a work done for a Fiverr client, that was of course well noticed of me being public with its content. This repository is still being updated.
A PowerPoint presentation could be found, explaining the work done in the project.

## Dataset
The UCF-Crime dataset is a large-scale dataset of 128 hours of videos. It consists of 1900 long and untrimmed real-world surveillance videos, with 13 realistic anomalies including Abuse, Arrest, Arson, Assault, Road Accident, Burglary, Explosion, Fighting, Robbery, Shooting, Stealing, Shoplifting, and Vandalism. These anomalies are selected because they have a significant impact on public safety.

Used feature extractor can be downloaded from: 
https://github.com/DavideA/c3d-pytorch

I3D features of UCF-Crime can be downloaded from: 
https://stuxidianeducn-my.sharepoint.com/:f:/g/personal/pengwu_stu_xidian_edu_cn/EvYcZ5rQZClGs_no2g-B0jcB4ynsonVQIreHIojNnUmPyA?e=xNrGxc

This dataset can be used for two tasks. First, general anomaly detection considering all anomalies in one group and all normal activities in another group. Second, for recognizing each of 13 anomalous activities.
We will concentrate on regognizing one anomaly, which is Shoplifting.


## Model

Pretrained model can be downloaded from : https://www.transferxl.com/download/08jQNW0dvpMcpt
Save it in \pretrained_models\ for a later use in testing.

The models architecture, and parts of code were originally taken from the public work of the Center for Research in Computer Vision : Real-world anomaly detection in Surveillance Videos (https://www.crcv.ucf.edu/research/real-world-anomaly-detection-in-surveillance-videos/)

All the code is well documented in the repo.


## Testing
After installing the required packages, a python script "test.py" could be ran and will load the downloaded pretrained model and saves the output in a dedicated folder.
A jupyter notebook "testing_steps.ipynb" is also present and contains all the needed steps for reproducing the results.

Examples of tagged videos could be found under "/outputs/tagged_videos"



