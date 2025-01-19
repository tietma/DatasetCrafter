import random 
import pandas as pd
from constants import ALLOWED_VAL_COL, WEIGHTS_COL

def generate_values(parameters: dict, num_values: int): 
    predefined_values = parameters.get(ALLOWED_VAL_COL)

    if pd.notna(predefined_values) and predefined_values != "nan":
        values = generate_categorial_data(parameters, num_values)
    else: 
        # if we do not have categorial values then we currently 
        # need to generate a distribution 
        values = list(range(0,100))

    return values


def generate_categorial_data(parameters: dict, num_values: int) -> list: 
    choices =  parameters.get(ALLOWED_VAL_COL, []).split(",")
    weights = parameters.get(WEIGHTS_COL, None).split(",")
    weights = [float(weight) for weight in weights]

    values = random.choices(choices,weights=weights, k=num_values)

    return values

 