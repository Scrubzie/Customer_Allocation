from customer_allocation import get_customer_allocation, create_dictionary
from route_partitioning import *
from route_solver import *
import pandas as pd

dataset = {
  'ID': [11, 12, 13, 14, 15, 16],
  'Customer': ["Woolworths Riverton", "Coles Karawara", "Spud Shed Jandakot", "Spud Shed Bentley", "Woolworths Innaloo", "Spud Shed Innaloo"]
}

runsheet = pd.DataFrame(dataset)

k = 3

if __name__=="__main__": 
    allocation_array = get_customer_allocation(runsheet, k)
    runsheet_dictionary = create_dictionary(runsheet)
    print(allocation_array)
    tree = None
    tree = partition_routes2(allocation_array, 1, runsheet_dictionary)
    print(allocation_array)
    print(tree)
    print(tree.post_order_dfs())
    tree.solve_tree()
    #print(runsheet_dictionary)

    
    # Check route for splitting                                                 (ROUTE PARTITIONING)
    # IF statement to check each individual route for additional splitting      (ROUTE PARTITIONING)
    
    # V2
    # (Create Distance Matrix)
    # Small enough route?                                                       (ROUTE SOLVER)
    #   Get our distance matrix, Comes from MapBox                              
    #   Send to QTSP
    #   Decipher answer
    # Large Route?                                                              (ROUTE SOLVER)
    #   Make a param for number of clusters, work out better method later, Dist.
    #   Solve the smaller clusters, Quantum
    #   Link starts and ends of each cluster
    #   Solve the bigger TSP, Quantum
    #   Decipher and combine large routes
    # Package them in some way for webapp to read?

    # From a tree perspective
    # Post Order Setup
      # If leaf, make distance matrix
    
    # Post Order Solution
      # If leaf, 
        # Make Matrix
        # Solve Matrix
      # If Parent,
        # Make Matrix
          # Grab start and end of each child
        # Solve Matrix