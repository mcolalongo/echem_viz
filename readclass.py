# no need for shebang as the class is imported in jupyternotebook and mypyvenv is selected afterwards. All good

import pandas as pd #lib for database management
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
import numpy as np, os

class Echem:

    def __init__(self, filepath, min_cycle, max_cycle):
        self.f = filepath # the constructor stores the filepath
        self.cmin = min_cycle
        self.cmax = max_cycle + 1
        self.range = np.arange(self.cmin, self.cmax)


    def extractData(self):
        for i in self.f:
            print(os.listdir())
        # self.df = pd.read_csv(self.f, sep=',')
        # return self.df
    