from pathlib import Path
import copy 
import pandas as pd
from typing import Hashable, Any
from file_writers import FileWriter
import constants as c

class DataSetCreator:
    """
    The DatasetCrafter is the core compofnent for creating datasets

    Attributes:
        schema (dict): schema of the dataset 

    """
    def __init__(self, schema: list[dict[Hashable, Any]]):
        self.schema = copy.deepcopy(schema)
        self.dataset = pd.DataFrame() 

    def _create_dataset(self):
        
        for entry in self.schema:
            self.dataset[entry.get(c.EXP_DATASET_COL)] = ""


    def generate_dataset(self):
        # @TODO check if input is parseable before dataset creation

        self._create_dataset()


class DataSetCreatorFactory: 
    """ 
    Factory to create DatsetCrafter instances

    Initially supported:
      - Instantiation via parameter dictionary 
      - Instantiation via csv file path 
    """

    @staticmethod
    def create(schema_source): 
        if isinstance(schema_source, dict):
            return DataSetCreator(schema_source)
        if isinstance(schema_source, pd.DataFrame):
            schema =  schema_source.to_dict(orient="records")
            return DataSetCreator(schema)
        if isinstance(schema_source, str): 
            path = Path(schema_source)
            if not path.is_file():
                raise FileNotFoundError(f"The provided file {schema_source} can't be found")
            if path.suffix != ".csv":
                raise ValueError(f"The provided file {schema_source} is not a csv file")
            schema = pd.read_csv(schema_source).to_dict(orient="records")
            return DataSetCreator(schema)
        

                