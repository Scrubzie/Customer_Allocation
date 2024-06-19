import numpy as np
import pandas as pd
from validation import *

#TODO Input Validation
#TODO Proper Params
#TODO Stub method for webapp format to pandas dataframe

LOWER_K = 0
UPPER_K = 10 #TODO This should be equal to samples in data

mydataset = {
  'ID': [1, 2, 3],
  'Customer': ["Woolworths Riverton", "Coles Karawara", "Spud Shed Jandakot"]
}

runsheet = pd.DataFrame(mydataset)

#TODO Try Catch Statement
def main(runsheet, k):
    #validate_runsheet(runsheet)

    #validate_k(k)
    validate_inputs(runsheet,2)
    #Validate Data

# Validate Data
#TODO Integer Check
def validate_k(k):
    if not isinstance(k,int):
        raise TypeError(f'Invalid k: must be an int. k is a {type(k)}')
    if not LOWER_K < k <= UPPER_K:
        raise ValueError(f'Invalid k: must be between {LOWER_K} and {UPPER_K}. k = ({k})')

#TODO Rename
# Dimension Check <>
# Label check?
# Check for Null entries
# Unique IDs
# Duplicate Check
# Format Check???
# Exists in Db
# Return a k-means ready distance matrix
# Need to keep track of which long/lat is for which entry (index-based)
"""
def validate_runsheet(runsheet):
    if runsheet.isnull().values.any():
        print("Null")
    else:
        print("No Nulls")
    print(runsheet.shape[0]) # Rows
    print(runsheet.shape[1]) # Columns
    # Right Format
    # Find Long and Lat per entry
"""
main(runsheet,5)