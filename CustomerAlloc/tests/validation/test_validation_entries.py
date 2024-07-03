import pytest
import sys
import os
import pandas as pd
import pyodbc
from validation import validate_inputs

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# pylint: disable=E0401
# False positive import error
from test_validation_fixtures import * # Wildcard, fix later

def test_null_check(runsheet_missing_value, testing_database):
    with pytest.raises(ValueError):  # 
        validate_inputs(runsheet_missing_value, 3, testing_database)

def test_label_names(runsheet_label_1, runsheet_label_2, runsheet_label_3, runsheet_label_case,
                     runsheet_label_null, testing_database):
    with pytest.raises(ValueError, match=r".* titles .*"):  # 
        validate_inputs(runsheet_label_1, 3, testing_database)
    with pytest.raises(ValueError, match=r".* titles .*"):  # 
        validate_inputs(runsheet_label_2, 3, testing_database)
    with pytest.raises(ValueError, match=r".* titles .*"):  # 
        validate_inputs(runsheet_label_3, 3, testing_database)
    with pytest.raises(ValueError, match=r".* titles .*"):  # 
        validate_inputs(runsheet_label_case, 3, testing_database)
    with pytest.raises(ValueError, match=r".* titles .*"):  # 
        validate_inputs(runsheet_label_null, 3, testing_database)

def test_unique_values(runsheet_duplicate_id, runsheet_duplicate_customer, testing_database):
    with pytest.raises(ValueError, match=r" *non-unique IDs.*"):  # 
        validate_inputs(runsheet_duplicate_id, 3, testing_database)
    with pytest.raises(ValueError, match=r" *non-unique Customers.*"):  # 
        validate_inputs(runsheet_duplicate_customer, 3, testing_database)
    runsheet_duplicate_id["Customer"] = runsheet_duplicate_customer["Customer"]
    with pytest.raises(ValueError, match=r" *non-unique IDs.*"):  # 
        validate_inputs(runsheet_duplicate_id, 3, testing_database)

def test_connection_string_driver(runsheet_valid, connection_string_wrong_driver):
    with pytest.raises(pyodbc.InterfaceError):  # 
        validate_inputs(runsheet_valid, 3, connection_string_wrong_driver)

@pytest.mark.slow
def test_connection_string_server(runsheet_valid, connection_string_wrong_server):
    with pytest.raises(pyodbc.OperationalError):  # 
        validate_inputs(runsheet_valid, 3, connection_string_wrong_server)

def test_connection_string_database(runsheet_valid, connection_string_wrong_database):
    with pytest.raises(pyodbc.InterfaceError):  # 
        validate_inputs(runsheet_valid, 3, connection_string_wrong_database)

def test_connection_string_uid(runsheet_valid, connection_string_wrong_uid):
    with pytest.raises(pyodbc.InterfaceError):  # 
        validate_inputs(runsheet_valid, 3, connection_string_wrong_uid)

def test_connection_string_pwd(runsheet_valid, connection_string_wrong_pwd):
    with pytest.raises(pyodbc.InterfaceError):  # 
        validate_inputs(runsheet_valid, 3, connection_string_wrong_pwd)

def test_no_entry(runsheet_fake_id, runsheet_fake_customer, testing_database):
    with pytest.raises(pyodbc.DatabaseError): #
        validate_inputs(runsheet_fake_id, 3, testing_database)
    with pytest.raises(ValueError, match=r" *does not match runsheet*"): #
        validate_inputs(runsheet_fake_customer, 3, testing_database)