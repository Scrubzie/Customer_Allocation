import pandas as pd
import pyodbc

from validation import validate_inputs

#TODO Input Validation 
#TODO Proper Params
#TODO Stub method for webapp format to pandas dataframe

mydataset = {
  'ID': [1, 2, 3],
  'Customer': ["Woolworths Riverton", "Coles Karawara", "Spud Shed Jandakot"]
}

runsheet = pd.DataFrame(mydataset)

SERVER = 'EAGLE-PREMIERS'
DATABASE = 'LocalQuantumTest'
USERNAME = 'agam'
PASSWORD = 'agam'

connectionString = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'

#TODO Try Catch Statement
def main(runsheet, k):
    validate_inputs(runsheet,k)
    runsheet_dictionary()
    geographic_array()
    geographic_to_cartesian()
    # Begin K-means

def example():
    cnxn = pyodbc.connect(connectionString)
    cursor = cnxn.cursor()	
    cursor.execute("SELECT * FROM Customer") 
    row = cursor.fetchone() 
    while row:
        print (row) 
        row = cursor.fetchone()
    cursor.close()
    cnxn.close()
    # Begin K-means

# Convert runsheet to geographic
# Assumed valid, will have to query Db for lat, long (index,[lat, long])
def geographic_array():
    print()

# Convert geographic to cartesian
# Simple math conversion
def geographic_to_cartesian():
    print()

# Create a dictionary that will map indices to ID
# Store it in memory
def runsheet_dictionary():
    print()

main(runsheet,2)

