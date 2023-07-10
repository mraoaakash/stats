import os
import pandas as pd
import numpy as np


path = "/storage/tnbc"
folders = os.listdir(path)
folders = [f for f in folders if "OPTRASCAN" in f]
print(folders)