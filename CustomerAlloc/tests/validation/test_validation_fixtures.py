import pytest
import pandas as pd

#Validate inputs(runsheet, k)

#format check
#- Type check <>
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
def runsheet_invalid_type():
    return "Hello"

@pytest.fixture
def runsheet_single_row():
    mydataset = {
        'ID': [1, 2, 3]
    }
    return pd.DataFrame(mydataset)

@pytest.fixture
def runsheet_three_rows():
    mydataset = {
        'ID': [1, 2, 3],
        'Customer': [4, 2, 1],
        'Name': ["Alpha", "Bravo", "Delta"]
    }
    return pd.DataFrame(mydataset)

@pytest.fixture
def testing_database():
    return "DRIVER={ODBC Driver 17 for SQL Server};SERVER=EAGLE-PREMIERS;\
        DATABASE=TestLocalQuantumTest;UID=agam;PWD=agam"

"""import pytest


def myfunc():
    raise ValueError("Exception 123 raised")


def test_match():
    with pytest.raises(ValueError, match=r".* 123 .*"):
        myfunc()"""