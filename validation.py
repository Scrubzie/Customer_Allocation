import pandas as pd
#Primary Function
# runsheet is pandas dataframe
# k is int
# Wrapper
def validate_inputs(runsheet, k):
    __validate_runsheet_format(runsheet)
    __validate_runsheet_entries(runsheet)
    total_customers = runsheet.shape[0] # total_customer = no. of rows
    __validate_k(k,total_customers)
    print()

# Format Check
# Null Check
# Dimension Check
# Label Name Check
# Unique IDs
# Unique Customer Names, in theory, duplicates are handled?

def __validate_runsheet_format(runsheet):
    """Verify the runsheet is in the correct format.
    The format must be a Pandas DataFrame with atleast 1 row and exactly 2 columns.

    :param pd.DataFrame runsheet: A runsheet containing IDs and customers

    :raises TypeError: If k is not an int
    :raises ValueError: If k is not between (and including) 1 and total_customers
    """
    if not isinstance(runsheet, pd.DataFrame):
        raise TypeError(f'runsheet must be in a dataframe.'
                        f'Runsheet = {type(runsheet)}')
    if not runsheet.shape[0] > 0:       # Must have atleast one customer
        raise ValueError(f'runsheet must contain atleast one customer.'
                         f'Runsheet has {runsheet.shape[0]} rows')
    if runsheet.shape[1] != 2:      # Must have two columns
        raise ValueError(f'runsheet must contain exactly two columns.'
                         f'Runsheet has {runsheet.shape[1]} columns')

def __validate_runsheet_entries(runsheet):
    labels = runsheet.columns.values
    if runsheet.isnull().values.any():      # Null check
        print("B")
        # Raise Exception
    if not (labels[0] == "ID" and labels[1] == "Customer"):
        print(runsheet.columns.values)
    if not runsheet['ID'].is_unique:
        print("E")
    if not runsheet['Customer'].is_unique:
        print("F")
    for row in runsheet.itertuples(index=False):
        customer_id = row[0]
        print(customer_id)
        # SQL CODE HERE
        # For each entry in dataframe, verify existence in db
        # EXISTS(SELECT * from <Table> WHERE ID=<ID_variable>);
        # If doesn't exist, raise exception
        # Else continue loop

#NOTE Done
def __validate_k(k, total_customers):
    """Verify that k is a valid value

    :param int k: The person sending the message
    :param int total_customers: The recipient of the message

    :raises TypeError: If k is not an int
    :raises ValueError: If k is not between (and including) 1 and total_customers
    """
    print(k, total_customers)
    if not isinstance(k, int):
        raise TypeError(f'k must be in an int. k = {type(k)}')
    if not 1 <= k <= total_customers:
        raise ValueError(f'k must be greater than 1 and less than total customers.'
                         f'k = {k}, total_customers = {total_customers}')
    