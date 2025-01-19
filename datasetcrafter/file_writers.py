import pandas as pd 
from abc import ABC
from abc import abstractmethod


class FileWriter(ABC):

    @abstractmethod
    def write_data(self, data):
        pass



class SingleFileWriter(FileWriter):

    def __init__(self, file_path, type="csv"):
        super().__init__()
        self.file_path = file_path
        self.type = type

    def write_data(self, dataset: pd.DataFrame):

        if self.type == "csv":
            dataset.to_csv(self.file_path, index=False)