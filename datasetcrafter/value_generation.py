import random 
import pandas as pd
from constants import ALLOWED_VAL_COL, WEIGHTS_COL, DIST_COL, RANGE_COL, DATA_TYPE_COL
import datetime 
from utils import convert_to_required_format

def generate_values(parameters: dict, num_values: int): 
    predefined_values = parameters.get(ALLOWED_VAL_COL)

    if pd.notna(predefined_values):
        values = generate_categorial_data(parameters, num_values)
    else:
        values = generate_distribution_data(parameters, num_values) 
        # if we do not have categorial values then we currently 
        # need to generate a distribution 

    return values

def generate_distribution_data(parameters: dict, num_values: int) -> list: 
    distribution = parameters.get(DIST_COL)




    if pd.notna(distribution): 
        pass
        # create set of values for specific distribution
    else:
        # create set of randomly sampled values
        values = generate_random_samples(parameters, num_values)

    return values


def generate_random_samples(parameters: dict, num_values: int) -> list:
    # first we identify 
    range_values = parameters.get(RANGE_COL).split("-")
    data_type = parameters.get(DATA_TYPE_COL)
    format = None
    min_val, max_val = convert_to_required_format(range_values, data_type, format=None)

    if data_type == "int":
        values = [random.randint(min_val, max_val) for _  in range(num_values)]
    elif data_type == "float":
        values = [random.uniform(min_val, max_val) for _ in range(num_values)]
    elif data_type == "datetime":
        pass 
    
    
    return values
    

def generate_categorial_data(parameters: dict, num_values: int) -> list: 

    choices =  parameters.get(ALLOWED_VAL_COL, []).split(",")
    weights = parameters.get(WEIGHTS_COL, None).split(",")
    weights = [float(weight) for weight in weights]

    values = random.choices(choices,weights=weights, k=num_values)

    return values