# -*- coding: utf-8 -*-

import numpy as np


class Population:
    """
    A Population is a measure over the the cells at given timepoint.

    Parameters
    ----------
    time : int or float
        The time at which the cells where measured.
    p : 1-D array-like
        Measure over the cells at the given timepoint.
    name : str
        Optional population name.
    """

    def __init__(self, time, p, name=None):
        self.time = time
        self.p = np.asarray(p, dtype=np.float64)
        self.name = name

    def normalize(self):
        """
        Make the measure sum to 1, i.e. be a probability distribution over cells.
        """
        self.p = self.p / self.p.sum()
