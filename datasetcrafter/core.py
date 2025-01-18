from pathlib import Path
import copy 

CHECK_SUM = 4

class DataSetCreator:
    """
    The DatasetCrafter is the core component for creating datasets

    Attributes:
        schema (dict): schema of the dataset 

    """
    def __init__(self, schema: dict):
        self.schema = copy.deepcopy(schema)



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
                