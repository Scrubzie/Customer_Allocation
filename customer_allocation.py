import pandas as pd
from validation import validate_inputs

#TODO Input Validation 
#TODO Proper Params
#TODO Stub method for webapp format to pandas dataframe

mydataset = {
  'ID': [1, 2, 3],
  'Customer': ["Woolworths Riverton", "Coles Karawara", "Spud Shed Jandakot"]
}

runsheet = pd.DataFrame(mydataset)

#TODO Try Catch Statement
def main(runsheet, k):
    validate_inputs(runsheet,k)
    runsheet_dictionary()
    geographic_array()
    geographic_to_cartesian()
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