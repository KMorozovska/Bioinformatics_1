from needlemanwunsch import *


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
    NW_matrix = np.array([[0, 0, 'S', 'U', 'M', 'O'],
                          [0, 0, -2, -4, -6, -8],
                          ['S', -2, 5, 3, 1, -1],
                          ['A', -4, 3, 1, -1, -3],
                          ['M', -6, 1, -1, 6, 4]], dtype=object)

    config['GAP'] = -2
    config['SAME'] = 5
    config['DIFF'] = -5
    seq_1 = "SAM"
    seq_2 = "SUMO"

    # when
    NW_table = NeedlemanWunsch(config, seq_1, seq_2)

    # then
    try:
        np.testing.assert_array_equal(NW_matrix, NW_table.matrix)
        print("Successfully created NW matrix ")
    except AssertionError as err:
        print(err)
        print("Error creating NW matrix")




def main():

    test_import_config('config.txt')
    test_create_NW_table()


if __name__ == "__main__":
    main()
