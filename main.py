from importlib.metadata import files
from pickletools import read_decimalnl_long
import numpy as np
import pandas as pd
import multiprocessing as mp
import threading
import os, os.path

s = pd.Series([1, 3, 5, np.nan, 6, 8])

print(s)

class Reader(threading.Thread):

    def __init__(self, files):
        super().__init__()
        self.files = files

    def run(self):
        

        for name in os.listdir('./dataset'):
            path = './dataset/' + name
            files[name] = pd.read_csv(path)
        pass

def main():
    files = {}

    reader = Reader(files)

    print(os.listdir('./dataset'))



    reader.start()
    reader.join()

    print(len(files))


if __name__ == '__main__':

    main()
