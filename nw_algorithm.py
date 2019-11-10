import numpy as np


class NeedlemanWunsch:


    def __init__(self, config, seq_1, seq_2):

        self.GAP = int(config['GAP'])
        self.SAME = int(config['SAME'])
        self.DIFF = int(config['DIFF'])
        self.seq_1 = seq_1
        self.seq_2 = seq_2
        self.matrix = np.zeros((len(seq_1)+2, len(seq_2)+2), dtype=object)

        self.fill_table()

        self.score = self.matrix[-1, -1]


    def fill_table(self):

        for i in range(self.matrix.shape[0]):
            for j in range(self.matrix.shape[1]):

                if i < len(self.seq_2) and j < len(self.seq_1):
                    self.matrix[0, i + 2] = self.seq_2[i]
                    self.matrix[j + 2, 0] = self.seq_1[j]

                if i > 1 and j > 1:
                    self.matrix[1, j] = self.matrix[1, j - 1] + self.GAP
                    self.matrix[i, 1] = self.matrix[i - 1, 1] + self.GAP

                    self.matrix[i, j] = max((self.matrix[i - 1, j - 1] + self.compare(self.matrix[0, j], self.matrix[i, 0])),
                                            (self.matrix[i - 1, j] + self.GAP),
                                            (self.matrix[i, j - 1] + self.GAP))



    def compare(self, val_1, val_2):
        if val_1 == val_2:
            return self.SAME
        else:
            return self.DIFF





