from import_files import *
from nw_algorithm import *


def test_import_config(filename):
    # given

    # when
    result = import_config(filename)
    # then
    if len(result) == 5:
        print("Successfully imported file")
    else:
        print("Error reading config file")



def test_create_NW_table():
    # given
    config = {'GAP': -2, 'SAME': 5, 'DIFF': -5}
    seq_1 = "SAM"
    seq_2 = "SUMO"

    NW_matrix = np.array([[0, 0, 'S', 'U', 'M', 'O'],
                          [0, 0, -2, -4, -6, -8],
                          ['S', -2, 5, 3, 1, -1],
                          ['A', -4, 3, 1, -1, -3],
                          ['M', -6, 1, -1, 6, 4]], dtype=object)

    # when
    NW_table = NeedlemanWunsch(config, seq_1, seq_2)

    # then
    try:
        np.testing.assert_array_equal(NW_matrix, NW_table.matrix)
        print("Successfully created NW matrix ")
    except AssertionError as err:
        print(err)
        print("Error creating NW matrix")



def test_adding_arrows():
    # given
    config = {'GAP': -2, 'SAME': 5, 'DIFF': -5}
    seq_1 = "SAM"
    seq_2 = "SUMO"

    NW_arrows = {((2, 2), (1, 1)): 5, ((2, 3), (2, 2)): 3, ((2, 4), (2, 3)): 1,((2, 5), (2, 4)): -1,
                 ((3, 2), (2, 2)): 3, ((3, 3), (2, 3)): 1, ((3, 3), (3, 2)): 1, ((3, 4), (2, 4)): -1,
                 ((3, 4), (3, 3)): -1, ((3, 5), (2, 5)): -3, ((3, 5), (3, 4)): -3, ((4, 2), (3, 2)): 1,
                 ((4, 3), (3, 3)): -1, ((4, 3), (4, 2)): -1, ((4, 4), (3, 3)): 6, ((4, 5), (4, 4)): 4}

    # when
    NW_table = NeedlemanWunsch(config, seq_1, seq_2)

    # then
    try:
        np.testing.assert_array_equal(NW_arrows, NW_table.arrows)
        print("Successfully created NW arrows ")
    except AssertionError as err:
        print(err)
        print("Error creating NW arrows")



def main():

    test_import_config('config.txt')
    test_create_NW_table()
    test_adding_arrows()


if __name__ == "__main__":
    main()
