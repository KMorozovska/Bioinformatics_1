import numpy as np


def fill_table(gap, same, diff, seq_1, seq_2):

    nw_matrix = np.zeros((len(seq_1)+2, len(seq_2)+2), dtype=object)

    for letter_1, letter_2, i, j in zip(seq_1, seq_2, range(2, len(seq_1) + 2), range(2, len(seq_2) + 2)):
        nw_matrix[0, i] = letter_1
        nw_matrix[j, 0] = letter_2

    for i in range(nw_matrix.shape[0]):
        for j in range(nw_matrix.shape[1]):
            if i > 1 and j > 1:
                nw_matrix[1, j] = nw_matrix[1, j - 1] + gap
                nw_matrix[j, 1] = nw_matrix[j - 1, 1] + gap


