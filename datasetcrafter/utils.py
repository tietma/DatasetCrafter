from dateutil import parser

# function used to convert values to a specified type and format
# if no format is provided, we assume a default format 
def convert_to_required_format(values: list, type, format=None):
    if type == "datetime":
        conv_values = [parser(value) for value in values]
    if type == "int" or type == "float":
        type_to_conv = eval(type)
        conv_values = [type_to_conv(value) for value in values]


    return conv_values