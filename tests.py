from import_files import *
from NeddlemanWunschMatrix import *
import sys


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
    NW_object = NeedlemanWunschMatrix(config, seq_1, seq_2)

    # then
    try:
        np.testing.assert_array_equal(NW_matrix, NW_object.matrix)
        print("Successfully created NW matrix ")
    except AssertionError as err:
        print(err)
        print("Error creating NW matrix")



def test_adding_arrows():
    # given
    config = {'GAP': -2, 'SAME': 5, 'DIFF': -5}
    seq_1 = "SAM"
    seq_2 = "SUMO"

    NW_arrows = [Arrow((2, 2), (1, 1), 0),
                 Arrow((2, 3), (2, 2), 5),
                 Arrow((2, 4), (2, 3), 3),
                 Arrow((2, 5), (2, 4), 1),
                 Arrow((3, 2), (2, 2), 5),
                 Arrow((3, 3), (3, 2), 3),
                 Arrow((3, 3), (2, 3), 3),
                 Arrow((3, 4), (3, 3), 1),
                 Arrow((3, 4), (2, 4), 1),
                 Arrow((3, 5), (3, 4), -1),
                 Arrow((3, 5), (2, 5), -1),
                 Arrow((4, 2), (3, 2), 3),
                 Arrow((4, 3), (4, 2), 1),
                 Arrow((4, 3), (3, 3), 1),
                 Arrow((4, 4), (3, 3), 1),
                 Arrow((4, 5), (4, 4), 6)]

    # when
    NW_table = NeedlemanWunschMatrix(config, seq_1, seq_2)

    # then
    try:
        np.testing.assert_array_equal(NW_arrows, NW_table.arrows)
        print("Successfully created NW arrows ")
    except AssertionError as err:
        print(err)
        print("Error creating NW arrows")



def test_create_graph():
    # given
    config = {'GAP': -2, 'SAME': 5, 'DIFF': -5}
    seq_1 = "SAM"
    seq_2 = "SUMO"

    NW_edges = [((2, 2), (1, 1)),
                 ((2, 3), (2, 2)),
                 ((2, 4), (2, 3)),
                 ((2, 5), (2, 4)),
                 ((3, 2), (2, 2)),
                 ((3, 3), (3, 2)),
                 ((3, 3), (2, 3)),
                 ((3, 4), (3, 3)),
                 ((3, 4), (2, 4)),
                 ((3, 5), (3, 4)),
                 ((3, 5), (2, 5)),
                 ((4, 2), (3, 2)),
                 ((4, 3), (4, 2)),
                 ((4, 3), (3, 3)),
                 ((4, 4), (3, 3)),
                 ((4, 5), (4, 4))]

    # when
    NW_table = NeedlemanWunschMatrix(config, seq_1, seq_2)

    # then
    try:
        np.testing.assert_array_equal(NW_edges, list(NW_table.G.edges))
        print("Successfully created NW directed graph ")
    except AssertionError as err:
        print(err)
        print("Error creating NW directed graph")




def main():

    if len(sys.argv) < 2:
        print("Please add argument with path to config_file.txt")
    else:
        config_path = sys.argv[1]

        test_import_config(config_path)
        test_create_NW_table()
        test_adding_arrows()
        test_create_graph()


if __name__ == "__main__":
    main()
