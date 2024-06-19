import pandas as pd
#Primary Function
# runsheet is pandas dataframe
# k is int
def validate_inputs(runsheet, k):
    __validate_runsheet(runsheet)
    #__validate_k()
    print()

def __validate_k(k, max_customers):
    print()

# Format Check
# Null Check
# Dimension Check
# Label Name Check
# Unique IDs
# Unique Customer Names, in theory, duplicates are handled?

def __validate_runsheet(runsheet):
    if not isinstance(runsheet, pd.DataFrame):
        # Raise Exception
        print("A")
    if runsheet.isnull().values.any():      # Null check
        print("B")
        # Raise Exception
    if not runsheet.shape[0] > 0:       # Must have atleast one customer
        print("C")
    if runsheet.shape[1] != 2:      # Must have two columns
        print("D")
    labels = runsheet.columns.values
    if not (labels[0] == "ID" and labels[1] == "Customer"):
        print(runsheet.columns.values)
    if not runsheet['ID'].is_unique:
        print("E")
    if not runsheet['Customer'].is_unique:
        print("F")
    # For each entry in dataframe, convert to 


#########################
#TODO Rename
# Dimension Check <>
# Label check? <>
# Check for Null entries <>
# Unique IDs <>
# Duplicate Check <>
# Format Check <>
# Exists in Db
# Return a k-means ready distance matrix
# Need to keep track of which long/lat is for which entry (index-based)
def validate_runsheet(runsheet):
    if runsheet.isnull().values.any():
        print("Null")
    else:
        print("No Nulls")
    print(runsheet.shape[0]) # Rows
    print(runsheet.shape[1]) # Columns
    # Right Format
    # Find Long and Lat per entry
