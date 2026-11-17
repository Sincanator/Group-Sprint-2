# Note: This code was written in google colab. It may need modification to be ran in local environment.

import kagglehub

from pathlib import Path
from fastai.vision.all import *

from sklearn.model_selection import train_test_split
from collections import Counter

import pandas as pd
from google.colab import files as colab_files

# Download datasets from Kaggle
danielshanbalico_dog_emotion_path = kagglehub.dataset_download('danielshanbalico/dog-emotion')
print(danielshanbalico_dog_emotion_path)
mohitagarwal17_dog_img_path = kagglehub.dataset_download('mohitagarwal17/dog-img')

searches = 'angry','happy','relaxed','sad'
path = Path('/kaggle/input/dog-emotion')

# Create train test split
path = Path("/kaggle/input/dog-emotion")
files = get_image_files(path)
train_files, test_files = train_test_split(
    files,
    test_size=0.10,
    random_state=42,
    stratify=[f.parent.name for f in files] # <- Addition to notebook
    )

print(len(train_files))
print(len(test_files))

# Checking the class distribution in data split
print("Training:", Counter(f.parent.name for f in train_files)) 
print("Testing:", Counter(f.parent.name for f in test_files))

# Create DataFrames
train_df = pd.DataFrame({
    "filename": [str(f.relative_to(path)) for f in train_files],
    "label": [f.parent.name for f in train_files]
})

test_df = pd.DataFrame({
    "filename": [str(f.relative_to(path)) for f in test_files],
    "label": [f.parent.name for f in test_files]
})

# Save CSVs
train_df.to_csv("development_split.csv", index=False)
test_df.to_csv("final_test_split.csv", index=False)

colab_files.download("development_split.csv")
colab_files.download("final_test_split.csv")
