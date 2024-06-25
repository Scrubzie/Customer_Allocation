import numpy as np
import pandas as pd
import pyodbc

from validation import validate_inputs
import database_connector as dc

#TODO Input Validation 
#TODO Proper Params
#TODO Stub method for webapp format to pandas dataframe

mydataset = {
  'ID': [1, 2, 3],
  'Customer': ["Woolworths Riverton", "Coles Karawara", "Spud Shed Jandakot"]
}

runsheet = pd.DataFrame(mydataset)

def main(runsheet, k):
    valid = False
    try:
        validate_inputs(runsheet,k)
        valid = True
    except (TypeError, ValueError, pyodbc.DatabaseError) as ex:
        print(ex)
    if valid:
        geo_array = __geographic_array(runsheet)            # np.array: [[Latitude,Longitude]]
        geo_array = geographic_to_cartesian(geo_array)      # np.array: [[x,y,z]]
        runsheet_dictionary = __create_dictionary(runsheet) # dictionary: [ID,CustomerName]
    else:
        # Raise Exception?
        print("Input was not valid")
    # Begin K-means

# Get geographic array
# Assumed valid, will have to query Db for lat, long (index,[lat, long])
# ProgrammingError for query
def __geographic_array(runsheet):
    conn = dc.DatabaseConnector()

    customer_ids = tuple(runsheet.iloc[:, 0]) # Tuple of customer IDs
    query = f'SELECT ID, latitude, longitude FROM Customer WHERE ID IN {customer_ids}'

    cursor = conn.create_cursor()
    cursor.execute(query)
    customer_data = cursor.fetchall()
    conn.close_cursor(cursor)

    # Create dictionary based on database result        
    customer_dict = {row[0]: (row[1], row[2]) for row in customer_data}

    # Init empty array
    array = np.zeros((runsheet.shape[0], 2))

    # Fill in array, get values from dictionary
    for counter, row in enumerate(runsheet.itertuples(index=False)):
        customer_location = customer_dict.get(row[0])
        if customer_location is None:
            raise pyodbc.DatabaseError(f'Entry does not exist. {row}')
        array[counter] = customer_location
    return array


# Convert geographic to cartesian
# Simple math conversion
def geographic_to_cartesian(geo_array):
    return("x")

# Create a dictionary that will map indices to ID
# Store it in memory
def __create_dictionary(dataframe):
    return {row[0]: row[1] for row in dataframe.values}

main(runsheet,2)
