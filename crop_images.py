from PIL import Image
import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np


def crop_images():

    dir = "train"

    filename = "attention_results.h5"
    df = pd.read_hdf(filename)
    counter = 0
    list_for_pandas = []

    a = df.iterrows()

    path = next(a)

    row_path = path[1].tolist()[0]
    full_dir_path = dir + "\\" + row_path.split("_")[0] + "\\" + row_path
    image = Image.open(full_dir_path)
    counter = 0

    for index, row in df.iterrows():

        if row['path'] != row_path:
            counter = 0
            row_path = row['path']
            full_dir_path = dir + "\\" + (row['path'].split("_"))[0]
            image = Image.open(full_dir_path + "\\" + row_path)

        if row['col'] == 'r':
            img2 = image.crop((row['x'] - 35*(1 - row['zoom']), row['y'] - 20*(1 - row['zoom']), row['x'] + 35*(1 - row['zoom']), row['y'] + 110*(1 - row['zoom'])))
            img2 = img2.resize((55, 105))
            img2.save("crops\\" + str(counter) + row['path'])
            counter += 1
            list_for_pandas.append((full_dir_path + "\\" + row['path'], row['x'] - 35*(1 - row['zoom']), row['y'] - 20*(1 - row['zoom']), row['x'] + 35*(1 - row['zoom']), row['y'] + 110*(1 - row['zoom']), row['col']))

        elif row['col'] == 'g':
            img2 = image.crop((row['x'] - 35*(1 - row['zoom']), row['y'] - 110*(1 - row['zoom']), row['x'] + 35*(1 - row['zoom']), row['y'] + 20*(1 - row['zoom'])))
            img2 = img2.resize((55, 105))
            img2.save("crops\\" + str(counter) + row['path'])
            counter += 1
            list_for_pandas.append((full_dir_path + "\\" + row['path'], row['x'] - 35*(1 - row['zoom']), row['y'] - 110*(1 - row['zoom']), row['x'] + 35*(1 - row['zoom']), row['y'] + 20*(1 - row['zoom']), row['col']))


    df1 = pd.DataFrame(list_for_pandas, columns=['fullPath', 'x0', 'y0', 'x1', 'y1', 'color'])
    df1.to_csv("croped_images.csv")


if __name__ == '__main__':
    crop_images()
