import numpy as np
import pandas as pd
import pyodbc
from sklearn.cluster import KMeans

from validation import validate_inputs
from geographic_processing import geographic_array, geographic_to_cartesian

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
        geo_array = geographic_array(runsheet)             # np.array: [[Latitude,Longitude]]
        cartesian_array = geographic_to_cartesian(geo_array) # np.array: [[x,y,z]]
        print(cartesian_array)
        runsheet_dictionary = __create_dictionary(runsheet)  # dictionary: [ID,CustomerName]
        __get_customer_allocation(k, cartesian_array)
    else:
        # Raise Exception?
        print("Input was not valid")

# Create a dictionary that will map indices to ID
# Store it in memory
def __create_dictionary(dataframe):
    return {row[0]: row[1] for row in dataframe.values}

# Do K-means++ on geo_array
# Output: [Index,assignment]
def __get_customer_allocation(k, geo_array):
    #print(type(geo_array))
    kmeans = KMeans(n_clusters=k, random_state=0, n_init="auto").fit(geo_array)
    print(kmeans.score(geo_array)) # Lower the score the better

    labels = kmeans.labels_ # This should be sufficient to 
    print(labels) # This should be sufficient to return
    print(type(labels))
    
    # Print the points assigned to each centroid
    for cluster in range(kmeans.n_clusters):
        print(f"Points assigned to centroid {cluster}:")
        for i, label in enumerate(labels):
            if label == cluster:
                print(f"Point {i}: {geo_array[i]}")
    return labels
    

main(runsheet,3)