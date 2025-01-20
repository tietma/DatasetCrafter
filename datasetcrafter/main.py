

import pandas as pd
import random 

from file_writers import SingleFileWriter
from core import DataSetCreatorFactory

def create_dummy_dataset(format_def_csv_path: str, file_output_path: str, num_entries: int, stratify_by=None):
    dsc = DataSetCreatorFactory.create(format_def_csv_path, num_entries)
    file_writer = SingleFileWriter(file_output_path)


    dsc.generate_dataset()
    file_writer.write_data(dsc.dataset)
    
    
if __name__ == "__main__":

    path_test_data = "/Users/matthias/test_data/test_data.csv"
    path_output = "/Users/matthias/generated/cars.csv"

    create_dummy_dataset(path_test_data, path_output, 100)
    print("done")

    