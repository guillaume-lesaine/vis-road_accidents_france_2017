import pytest
import json
import pandas as pd
import pandas.util.testing as tm
import inspect
from package import functions


####### Preparation

# Load test_functions_parameters.json containing the scenarios for the tests

with open("./tests/json/test_functions_parameters.json", 'r') as f:
    dictionary_json = json.load(f)

def discover_function(z):
    function = inspect.getframeinfo(z).function.replace("test_","")
    method = getattr(functions, function)
    return function, method

def load_json(filename,case):
    with open("./tests/json/" + filename, 'r') as f:
        dict = json.load(f)[case]
        if len(dict) == 1:
            data = dict[next(iter(dict))]
        else :
            data = tuple(dict.values())
    return data

def load_csv(filename):
    df = pd.read_csv("./tests/csv/" + filename)
    return df

####### Tests

arguments, values = dictionary_json["victims_stacked"].values()
@pytest.mark.parametrize(arguments, values)
def test_victims_stacked(df_filename, l_filename, case, df_result_filename):
    function, method = discover_function(inspect.currentframe())

    '''
        Test function of victims_stacked.
    '''

    df, df_result = load_csv(df_filename), load_csv(df_result_filename)
    l = load_json(l_filename, case)

    df_output = method(df, l)

    tm.assert_frame_equal(df_output, df_result)
