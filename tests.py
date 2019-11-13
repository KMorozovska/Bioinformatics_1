from prepare_files import *
from NeddlemanWunschMatrix import *
import sys


def test_import_config(filename):
    # given

    # when
    result = import_config(filename)
    # then
    if len(result) == 5 and {"gap", "same", "diff", "max_seq_length", "max_number_paths"} <= set(result):
        print("Successfully imported file\n")
    else:
        print("Error reading config file\n")



def test_create_NW_table():
    # given
    config = {'gap': -2, 'same': 5, 'diff': -5, 'max_number_paths': 10}
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
        print("Successfully created NW matrix\n")
    except AssertionError as err:
        print(err)
        print("Error creating NW matrix\n")



def test_adding_arrows():
    # given
    config = {'gap': -2, 'same': 5, 'diff': -5, 'max_number_paths': 10}
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
        print("Successfully created NW arrows\n")
    except AssertionError as err:
        print(err)
        print("Error creating NW arrows\n")



def test_create_graph():
    # given
    config = {'gap': -2, 'same': 5, 'diff': -5, 'max_number_paths': 10}
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
        print("Successfully created NW directed graph\n")
    except AssertionError as err:
        print(err)
        print("Error creating NW directed graph\n")




def main():

    if len(sys.argv) < 2:
        print("Please add argument with path to config.txt")
    else:
        config_path = sys.argv[1]

        test_import_config(config_path)
        test_create_NW_table()
        test_adding_arrows()
        test_create_graph()


if __name__ == "__main__":
    main()
