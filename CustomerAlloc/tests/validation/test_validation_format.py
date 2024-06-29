import pytest
import sys
import os
import pandas as pd
from validation import validate_inputs

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# pylint: disable=E0401
# False positive import error
from test_validation_fixtures import * # Wildcard, fix later

@pytest.mark.parametrize("k_values", [
    1,
    3,
    5
])
def test_valid_runsheet(runsheet_valid, k_values, testing_database):
    try:
        validate_inputs(runsheet_valid, k_values, testing_database)
    except Exception as e:
        pytest.fail(f"Function raised an unexpected exception: {e}")

def test_invalid_types(runsheet_invalid_type, testing_database):
    with pytest.raises(TypeError):  # String Test
        validate_inputs(runsheet_invalid_type, 3, testing_database)
    with pytest.raises(TypeError):  # Null Test
        validate_inputs(None, 3, testing_database)

def test_row_count(runsheet_valid,testing_database):
    runsheet_valid = runsheet_valid.head(1) # 1 row runsheet
    try:
        validate_inputs(runsheet_valid,1, testing_database)
    except Exception as e:
        pytest.fail(f"Function raised an unexpected exception: {e}")

    df = pd.DataFrame() # 0 row runsheet
    with pytest.raises(ValueError):
        validate_inputs(df, 3, testing_database)

def test_column_count():
    print()
    # 0,1,2,3
