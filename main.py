#TODO Input Validation
#TODO Proper Params

LOWER_K = 0
UPPER_K = 10 #TODO This should be equal to samples in data

#TODO Try Catch Statement
def main(runsheet, k):
    validate_k(k)
    validate_data(runsheet)
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
    #Right Format
    #Find Long and Lat per entry

def 

main(5,5)
