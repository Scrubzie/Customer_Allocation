import itertools

def calculate_tour_cost(tour, dist_matrix):
    """Calculate the cost of a given tour based on the distance matrix."""
    cost = 0
    num_cities = len(tour)
    for i in range(num_cities):
        cost += dist_matrix[tour[i]][tour[(i + 1) % num_cities]]
    return cost

def brute_force_atsp(dist_matrix):
    """Brute force approach to solve the ATSP."""
    num_cities = len(dist_matrix)
    all_tours = itertools.permutations(range(num_cities))
    min_cost = float('inf')
    best_tour = None

    for tour in all_tours:
        tour_cost = calculate_tour_cost(tour, dist_matrix)
        if tour_cost < min_cost:
            min_cost = tour_cost
            best_tour = tour

    return best_tour, min_cost

# Example usage:
if __name__ == "__main__":
    # Example distance matrix
    dist_matrix = [
        [0, 10, 15],
        [5, 0, 9],
        [6, 13, 0]
    ]

    best_tour, min_cost = brute_force_atsp(dist_matrix)
    print("Best tour:", best_tour)
    print("Minimum cost:", min_cost)