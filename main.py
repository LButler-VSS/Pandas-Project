from pickletools import read_decimalnl_long
import numpy as np
import pandas as pd
import multiprocessing as mp
import threading
import os, os.path

s = pd.Series([1, 3, 5, np.nan, 6, 8])

print(s)

class Reader(threading.Thread):
    """ This is a dealer that receives cars """

    def __init__(self):
        super().__init__()

    def run(self):
        for i in range(len(os.listdir('./dataset'))):
            pd.read_csv()
        pass

def main():
    reader = Reader()

    print(len(os.listdir('./dataset')))

    reader.start()
    reader.join()



if __name__ == '__main__':

    main()
