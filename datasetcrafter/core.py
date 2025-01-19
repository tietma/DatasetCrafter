from pathlib import Path
import copy 
import pandas as pd

from file_writers import FileWriter

class DataSetCreator:
    """
    The DatasetCrafter is the core compofnent for creating datasets

    Attributes:
        schema (dict): schema of the dataset 

    """
    def __init__(self, schema: dict):
        self.schema = copy.deepcopy(schema)

    def _create_dataset(self):
        self.dataset = pd.DataFrame.from_dict(self.schema)

    def generate_dataset(self):
        self._create_dataset()


class DataSetCreatorFactory: 
    """ 
    Factory to create DatsetCrafter instances

    Initially supported:
      - Instantiation via parameter dictionary 
      - Instantiation via csv file path 
    dfsoadfslk
    """
    @staticmethod
    def create(schema_source): 
        if isinstance(schema_source, dict):
            return DataSetCreator(schema_source)
        if isinstance(schema_source, str): 
            path = Path(schema_source)
            if not path.is_file():
                raise FileNotFoundError(f"The provided file {schema_source} can't be found")
            if path.suffix != ".csv":
                raise ValueError(f"The provided file {schema_source} is not a csv file")
            
            schema = pd.read_csv(schema_source).to_dict()
            return DataSetCreator(schema)
                