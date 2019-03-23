import os
import pandas as pd

#creating a root directory
rootdir = "N:/Research/RW/Employee Contracts/pgm/employment contracts/"
file_list = list()

for root, dirs, files in os.walk(rootdir):
    for file in files:
        if file.endswith(".txt"):
            with open(os.path.join(root, file), encoding="latin-1") as f:
                f = os.path.splitext(file)[0]
                time_txt = f.split('_')
                file_list.append(time_txt[2])

print(file_list)

#making a dataset
df = pd.DataFrame(file_list)
df.to_csv("N:/Research/RW/Employee Contracts/pgm/dataset/files/dataset.csv", encoding='utf-8', index=False, sep=' ', header=False)