import numpy as np
from Arrow import *
import networkx as nx


class NeedlemanWunschMatrix:

    def __init__(self, config, seq_1, seq_2):

        self.GAP = int(config['GAP'])
        self.SAME = int(config['SAME'])
        self.DIFF = int(config['DIFF'])
        self.seq_1 = seq_1
        self.seq_2 = seq_2
        self.matrix = np.zeros((len(seq_1) + 2, len(seq_2) + 2), dtype=object)
        self.arrows = []
        self.G = nx.DiGraph()
        self.best_paths = []

        self.fill_matrix()

        self.final_score = self.matrix[-1, -1]

        self.find_best_paths()
        self.prepare_output()


    def fill_matrix(self):
        """ Function preparing NeedlemanWunsch matrix, from filling the letters to finding the score. """

        for i in range(self.matrix.shape[0]):
            for j in range(self.matrix.shape[1]):

                if i < len(self.seq_2) and j < len(self.seq_1):
                    self.matrix[0, i + 2] = self.seq_2[i]
                    self.matrix[j + 2, 0] = self.seq_1[j]

                if i > 1 and j > 1:
                    self.matrix[1, j] = self.matrix[1, j - 1] + self.GAP
                    self.matrix[i, 1] = self.matrix[i - 1, 1] + self.GAP

                    diag = (self.matrix[i - 1, j - 1] + self.compare(self.matrix[0, j], self.matrix[i, 0]))
                    up = (self.matrix[i, j - 1] + self.GAP)
                    left = (self.matrix[i - 1, j] + self.GAP)

                    selected = max(diag, up, left)

                    self.add_arrow(i, j, diag, up, left, selected)

                    self.matrix[i, j] = selected

    def compare(self, val_1, val_2):
        if val_1 == val_2:
            return self.SAME
        else:
            return self.DIFF

    def add_arrow(self, i, j, diag, up, left, selected):
        """ Arrow list is created as a list of Arrow objects,
         containing: selected cell co-ordinates, source co-ordinates and value in selected cell """

        if diag == selected:
            self.arrows.append(Arrow((i, j), (i - 1, j - 1), self.matrix[i - 1, j - 1]))
            self.G.add_edge((i, j), (i - 1, j - 1), weight=self.matrix[i - 1, j - 1])
        if up == selected:
            self.arrows.append(Arrow((i, j), (i, j - 1), self.matrix[i, j - 1]))
            self.G.add_edge((i, j), (i, j - 1), weight=self.matrix[i, j - 1])
        if left == selected:
            self.arrows.append(Arrow((i, j), (i - 1, j), self.matrix[i - 1, j]))
            self.G.add_edge((i, j), (i - 1, j), weight=self.matrix[i - 1, j])


    def find_best_paths(self):

        all_paths = nx.all_simple_paths(self.G, source=(self.matrix.shape[0]-1, self.matrix.shape[1]-1), target=(1, 1))

        scores_dict = {}
        k = 0
        for path in all_paths:

            score = 0

            for i in range(len(path) - 1):
                arr_list = [obj for obj in self.arrows if obj.source == path[i] and obj.dest == path[i + 1]]
                if len(arr_list) > 0:
                    next_arrow = arr_list[0]
                    score += next_arrow.value

            scores_dict[k] = score
            k += 1

        max_value = max(scores_dict.values())
        best_paths_ids = [k for k, v in scores_dict.items() if v == max_value]

        i = 0
        for path in nx.all_simple_paths(self.G, source=(self.matrix.shape[0]-1, self.matrix.shape[1]-1), target=(1, 1)):

            if i in best_paths_ids:
                self.best_paths.append(path)
            i += 1



    def prepare_output(self):

        print(self.best_paths)