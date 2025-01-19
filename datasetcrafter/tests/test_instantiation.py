

import pandas as pd
import pytest
import tempfile
import os

from core import DataSetCreator
from core import DataSetCreatorFactory


@pytest.fixture
def csv_file_path():
    """
    Create a temporary csv file from a mock dataframe

    Yields:
        str: The file path to the created csv file
    """
    df_mock = pd.DataFrame({"column_names": ["car_type", "color", "cost"],
                            "data_type":["str", "str", "float"], 
                            "range": ["", "", "5000-120000"]})

    with tempfile.NamedTemporaryFile(mode="w+", suffix=".csv", delete=False) as temp_file:
        df_mock.to_csv(temp_file.name, index=False)
        
        temp_file.seek(0)
        yield temp_file.name

    os.remove(temp_file.name)

def test_csv_instantiation(csv_file_path):
    param = pd.read_csv(csv_file_path).to_dict()
    
    dsc = DataSetCreator(param, 100)

    assert param == dsc.schema


def test_factory_instantiation_existing_path(csv_file_path):
    dsc = DataSetCreatorFactory.create(csv_file_path, 100)


def test_factory_non_existing_file_path():
    with pytest.raises(FileNotFoundError):
        dsc = DataSetCreatorFactory.create("invalid_schema_source", 100) 





    
