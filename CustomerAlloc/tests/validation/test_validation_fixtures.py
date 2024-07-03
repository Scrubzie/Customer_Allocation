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
def runsheet_missing_value():
    return pd.DataFrame({
        'ID': [1, 3 , 10, 502, 214],
        'Customer': ["Alpha", None, "Charlie", "Delta", "Echo"]
    })

@pytest.fixture
def runsheet_label_1():
    return pd.DataFrame({
        'X': [1, 3 , 10, 502, 214],
        'Customer': ["Alpha", "Bravo", "Charlie", "Delta", "Echo"]
    })

@pytest.fixture
def runsheet_label_2():
    return pd.DataFrame({
        'ID': [1, 3 , 10, 502, 214],
        'Y': ["Alpha", "Bravo", "Charlie", "Delta", "Echo"]
    })

@pytest.fixture
def runsheet_label_3():
    return pd.DataFrame({
        'X': [1, 3 , 10, 502, 214],
        'H': ["Alpha", "Bravo", "Charlie", "Delta", "Echo"]
    })

@pytest.fixture
def runsheet_label_case():
    return pd.DataFrame({
        'id': [1, 3 , 10, 502, 214],
        'customer': ["Alpha", "Bravo", "Charlie", "Delta", "Echo"]
    })

@pytest.fixture
def runsheet_label_null():
    return pd.DataFrame({
        None: [1, 3 , 10, 502, 214],
        'customer': ["Alpha", "Bravo", "Charlie", "Delta", "Echo"]
    })

@pytest.fixture
def runsheet_duplicate_id():
    return pd.DataFrame({
        'ID': [1, 3 , 10, 502, 3],
        'Customer': ["Alpha", "Bravo", "Charlie", "Delta", "Echo"]
    })

@pytest.fixture
def runsheet_duplicate_customer():
    return pd.DataFrame({
        'ID': [1, 3 , 10, 502, 214],
        'Customer': ["Alpha", "Bravo", "Charlie", "Bravo", "Echo"]
    })

@pytest.fixture
def runsheet_fake_id():
    return pd.DataFrame({
        'ID': [1, 33333 , 10, 502, 214],
        'Customer': ["Alpha", "Bravo", "Charlie", "Delta", "Echo"]
    })

@pytest.fixture
def runsheet_fake_customer():
    return pd.DataFrame({
        'ID': [1, 3 , 10, 502, 214],
        'Customer': ["Alpha", "Bravo", "Zulu", "Delta", "Echo"]
    })

@pytest.fixture
def runsheet_one_entry():
    return pd.DataFrame({
        'ID': [1],
        'Customer': ["Alpha"]
    })

@pytest.fixture
def runsheet_two_entries():
    return pd.DataFrame({
        'ID': [1, 3],
        'Customer': ["Alpha", "Bravo"]
    })

@pytest.fixture
def testing_database():
    return "DRIVER={ODBC Driver 17 for SQL Server};SERVER=EAGLE-PREMIERS;\
        DATABASE=TestLocalQuantumTest;UID=agam;PWD=agam"

@pytest.fixture
def connection_string_wrong_driver():
    return "DRIVER={ODBC Driver 16 for SQL Server};SERVER=EAGLE-PREMIERS;\
        DATABASE=TestLocalQuantumTest;UID=agam;PWD=agam"

@pytest.fixture
def connection_string_wrong_server():
    return "DRIVER={ODBC Driver 17 for SQL Server};SERVER=EAGXLE-PREMIERS;\
        DATABASE=TestLocalQuantumTest;UID=agam;PWD=agam"

@pytest.fixture
def connection_string_wrong_database():
    return "DRIVER={ODBC Driver 17 for SQL Server};SERVER=EAGLE-PREMIERS;\
        DATABASE=TestLocXalQuantumTest;UID=agam;PWD=agam"

@pytest.fixture
def connection_string_wrong_uid():
    return "DRIVER={ODBC Driver 17 for SQL Server};SERVER=EAGLE-PREMIERS;\
        DATABASE=TestLocalQuantumTest;UID=agaam;PWD=agam"

@pytest.fixture
def connection_string_wrong_pwd():
    return "DRIVER={ODBC Driver 17 for SQL Server};SERVER=EAGLE-PREMIERS;\
        DATABASE=TestLocalQuantumTest;UID=agam;PWD=agammm"

#DRIVER={ODBC Driver 17 for SQL Server};SERVER=EAGLE-PREMIERS;DATABASE=TestLocalQuantumTest;UID=agam;PWD=agam
    # Wrong Driver
    # Wrong Format
    # Wrong Server
    # Wrong Database
    # Wrong UID
    # Wrong PWD