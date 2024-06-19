import numpy as np
import pandas as pd

#TODO Input Validation
#TODO Proper Params

RUNSHEET = ["Woolworths","Coles","Spud Shed"]

LOWER_K = 0
UPPER_K = 10 #TODO This should be equal to samples in data

#TODO Try Catch Statement
def main(runsheet, k):
    customer_array = validate_runsheet(runsheet)

    validate_k(k)
    #Validate Data

# Validate Data
#TODO Integer Check
def validate_k(k):
    if not isinstance(k,int):
        raise TypeError(f'Invalid k: must be an int. k is a {type(k)}')
    if not (LOWER_K < k <= UPPER_K):
        raise ValueError(f'Invalid k: must be between {LOWER_K} and {UPPER_K}. k = ({k})')

#TODO Rename
def validate_runsheet(runsheet):
    print("Not Implemented Yet")
    print(type(runsheet))
    return np.array(runsheet)
    # Right Format
    # Find Long and Lat per entry

main(RUNSHEET,5)

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)