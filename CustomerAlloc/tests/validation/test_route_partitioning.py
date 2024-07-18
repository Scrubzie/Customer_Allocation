from route_partitioning import insert_into_array


def test_insert_into_array():
    old_array = [5, 2, 1, 52, 1, 5, 1, 1]
    new_array = [-1, -1, -1, -1, -1, -1, -1, -1]
    new_array = insert_into_array(new_array, old_array, 1)
    assert new_array == [-1, -1, 1, -1, 1, -1, 1, 1]