"""
Tests to ensure that given data parameter input 
leads to the expected dataset output 
"""
import pandas as pd
import pytest
import tempfile
import os

from constants import EXP_DATASET_COL
from core import DataSetCreatorFactory

def test_dataset_specified_columns_present():
    df_mock = pd.DataFrame({EXP_DATASET_COL: ["car_type", "color", "cost"],
                            "data_type":["str", "str", "float"], 
                            "range": ["", "", "5000-120000"]})
    dsc = DataSetCreatorFactory.create(df_mock)
    dsc.generate_dataset()

    columns_required = df_mock[EXP_DATASET_COL]

    assert set(columns_required) == set(dsc.dataset.columns)
        