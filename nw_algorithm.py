import numpy as np


class NeedlemanWunsch:


    def __init__(self, config, seq_1, seq_2):

        self.GAP = int(config['GAP'])
        self.SAME = int(config['SAME'])
        self.DIFF = int(config['DIFF'])
        self.seq_1 = seq_1
        self.seq_2 = seq_2
        self.matrix = np.zeros((len(seq_1)+2, len(seq_2)+2), dtype=object)
        self.arrows = {}

        self.fill_table()

        self.score = self.matrix[-1, -1]


    def fill_table(self):
        """ Function preparing NeedlemanWunsch matrix, from filling the letters to finding the score. """

        for i in range(self.matrix.shape[0]):
            for j in range(self.matrix.shape[1]):

                if i < len(self.seq_2) and j < len(self.seq_1):
                    self.matrix[0, i+2] = self.seq_2[i]
                    self.matrix[j+2, 0] = self.seq_1[j]

                if i > 1 and j > 1:
                    self.matrix[1, j] = self.matrix[1, j-1] + self.GAP
                    self.matrix[i, 1] = self.matrix[i-1, 1] + self.GAP

                    diag = (self.matrix[i-1, j-1] + self.compare(self.matrix[0, j], self.matrix[i, 0]))
                    up = (self.matrix[i-1, j] + self.GAP)
                    left = (self.matrix[i, j-1] + self.GAP)

                    selected = max(diag, up, left)

                    self.add_arrow(i, j, diag, up, left, selected)

                    self.matrix[i, j] = selected



    def compare(self, val_1, val_2):
        if val_1 == val_2:
            return self.SAME
        else:
            return self.DIFF


    def add_arrow(self, i, j, diag, up, left, selected):
        """ Arrow dictionary is created as a key-value pair of:
        tuple of tuples (selected cell co-ordinates, source co-ordinates) : value in selected cell """

        if diag == selected:
            self.arrows[((i, j), (i-1, j-1))] = selected
        if up == selected:
            self.arrows[((i, j), (i-1, j))] = selected
        if left == selected:
            self.arrows[((i, j), (i, j-1))] = selected








