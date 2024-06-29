import pytest
import pandas as pd
from validation import validate_inputs

#Validate inputs(runsheet, k)

#format check
#- Type check
#- Row check
#- Column check

#entries
#- Null values
#- Column name check
#- Unique IDs
#- Unique Customers
#- All entries exists
#- Some exist
#- None Exist

#validate_k
#- Type check
#- Bound checking k and customers

@pytest.fixture
def runsheet_valid():
    return pd.DataFrame({
        'ID': [1, 3 , 10, 502, 214],
        'Customer': ["Alpha", "Bravo", "Charlie", "Delta", "Echo"]
    })

@pytest.fixture
def testing_database():
    return "DRIVER={ODBC Driver 17 for SQL Server};SERVER=EAGLE-PREMIERS;\
        DATABASE=TestLocalQuantumTest;UID=agam;PWD=agam"

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



"""import pytest


def myfunc():
    raise ValueError("Exception 123 raised")


def test_match():
    with pytest.raises(ValueError, match=r".* 123 .*"):
        myfunc()"""