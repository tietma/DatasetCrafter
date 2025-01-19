from pathlib import Path
import copy 
import pandas as pd
from typing import Hashable, Any
import constants as c
from value_generation import generate_values

class DataSetCreator:
    """
    The DatasetCrafter is the core compofnent for creating datasets

    Attributes:
        schema (dict): schema of the dataset 

    """
    def __init__(self, schema: list[dict[Hashable, Any]], num_entries, stratify_by=None):
        self.schema = copy.deepcopy(schema)
        self.num_entries = num_entries
        self.dataset = pd.DataFrame() 
        self.stratify_by = stratify_by

    def _create_dataset(self):
        if self.stratify_by:
            print("stratification required")
        for entry in self.schema:
            exp_col_name = entry.get(c.EXP_DATASET_COL)

            values = generate_values(entry, self.num_entries)
            self.dataset[exp_col_name] = values
            


    def generate_dataset(self):
        # @TODO check if input is parseable before dataset creation

        self._create_dataset()
        print(self.dataset)


class DataSetCreatorFactory: 
    """ 
    Factory to create DatsetCrafter instances

    Initially supported:
      - Instantiation via parameter dictionary 
      - Instantiation via csv file path 
    """

    @staticmethod
    def create(schema_source, num_entries): 
        if isinstance(schema_source, dict):
            schema = schema_source
        if isinstance(schema_source, pd.DataFrame):
            schema =  schema_source.to_dict(orient="records")

        if isinstance(schema_source, str): 
            path = Path(schema_source)
            if not path.is_file():
                raise FileNotFoundError(f"The provided file {schema_source} can't be found")
            if path.suffix != ".csv":
                raise ValueError(f"The provided file {schema_source} is not a csv file")
            schema = pd.read_csv(schema_source).to_dict(orient="records")
            
        
        return DataSetCreator(schema, num_entries=num_entries)
        

                