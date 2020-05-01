import subprocess
import os

SegmentFolderPathList = ['/home/ubuntu/Research/Antifreeze/Sample_Videos/ML/Segments']

for folder in SegmentFolderPathList:
    segments = sorted(list(os.listdir(folder)))
    print(segments)