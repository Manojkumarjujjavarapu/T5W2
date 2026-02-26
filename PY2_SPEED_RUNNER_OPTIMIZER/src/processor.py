import os
import pandas as pd
from multiprocessing import Pool


def read_file_generator(file_path):
    
    
    for chunk in pd.read_csv(file_path, chunksize=1000):
        yield chunk


def process_file(file_path):
    
    total = 0

    for chunk in read_file_generator(file_path):
        values = chunk["value"].tolist()

        for v in values:
            for _ in range(200):  
                total += (v * v) % 97

    return total


def baseline_process(folder_path):
    files = [
        os.path.join(folder_path, f)
        for f in os.listdir(folder_path)
        if f.endswith(".csv")
    ]

    results = []

    for file in files:
        results.append(process_file(file))

    return len(files)


def multiprocessing_process(folder_path):
    files = [
        os.path.join(folder_path, f)
        for f in os.listdir(folder_path)
        if f.endswith(".csv")
    ]

    with Pool() as pool:
        pool.map(process_file, files)

    return len(files)