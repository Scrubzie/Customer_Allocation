import pytest
import sys
import os
import pandas as pd
from validation import validate_inputs

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# pylint: disable=E0401
# False positive import error
from test_validation_fixtures import * # Wildcard, fix later

def test_k_null_check(runsheet_valid, testing_database):
    with pytest.raises(TypeError):  # 
        validate_inputs(runsheet_valid, None, testing_database)

# Could param this
def test_k_type(runsheet_valid, testing_database):
    with pytest.raises(TypeError):  # 
        validate_inputs(runsheet_valid, "Two", testing_database)
    with pytest.raises(TypeError):  # 
        validate_inputs(runsheet_valid, 2.63, testing_database)
    validate_inputs(runsheet_valid, 2, testing_database)

# 1 <= k <= total_customers
# 1 1 1
# 1 1 2
# 1 2 1
# 1 2 2
# 1 -1 1
# 1 0 1

def test_k_bounds(runsheet_one_entry, runsheet_two_entries, testing_database):
    validate_inputs(runsheet_one_entry, 1, testing_database)
    validate_inputs(runsheet_two_entries, 1, testing_database)
    with pytest.raises(ValueError):  # 
        validate_inputs(runsheet_one_entry, 2, testing_database)
    validate_inputs(runsheet_two_entries, 2, testing_database)
    with pytest.raises(ValueError):  # 
        validate_inputs(runsheet_one_entry, -1, testing_database)
    with pytest.raises(ValueError):  # 
        validate_inputs(runsheet_one_entry, 0, testing_database)