import numpy as np
import pyodbc

import database_connector as dc

# Get geographic array
# Assumed valid, will have to query Db for lat, long (index,[lat, long])
# ProgrammingError for query
def geographic_array(runsheet, connection_string):
    conn = dc.DatabaseConnector(connection_string)

    customer_ids = tuple(runsheet.iloc[:, 0]) # Tuple of customer IDs

    if len(customer_ids) == 1:
        customer_ids = f"({customer_ids[0]})"

    query = f'SELECT ID, latitude, longitude FROM Customer WHERE ID IN {customer_ids}'

    cursor = conn.create_cursor()
    #print(query)
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
    cartesian_array = np.zeros((geo_array.shape[0],3))
    for index, x in enumerate(geo_array):
        cartesian_coord = __get_cartesian(x[0],x[1])
        cartesian_array[index] = cartesian_coord
    return cartesian_array

def __get_cartesian(lat=None,lon=None):
    lat, lon = np.deg2rad(lat), np.deg2rad(lon)
    R = 6371 # radius of the earth
    x = R * np.cos(lat) * np.cos(lon)
    y = R * np.cos(lat) * np.sin(lon)
    z = R *np.sin(lat)
    return np.array((x,y,z))