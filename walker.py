import os
import pandas as pd
import numpy as np


path = "/storage/tnbc"
folders = os.listdir(path)
folders = [f for f in folders if "OPTRASCAN" in f]
print(folders)
images = []
paths = []
for folder in folders:
    for root, dirs, files in os.walk(os.path.join(path, folder)):
        for file in files:
            if file.endswith(".tif"):
                images.append(file)
                paths.append(os.path.join(root, file))

df = pd.DataFrame({"image": images, "path": paths})
df.to_csv("/home/rintu.kutum/stats/tnbc.csv", index=False)
df.to_excel("/home/rintu.kutum/stats/tnbc.xlsx", index=False)