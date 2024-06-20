import numpy as np
import pandas as pd
from validation import *

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
    #validate_runsheet(runsheet)

    #validate_k(k)
    validate_inputs(runsheet,4)
    #Validate Data

main(runsheet,5)