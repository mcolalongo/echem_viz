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


    def plotDqDv(self):
        self.fig, self.ax = plt.subplots(dpi=100, figsize=(4,3)) 
        for j in self.range:
            for i in os.listdir(self.f):
                if (f"cycle_{j}.csv") in i:
                    self.df = pd.read_csv(os.path.join(self.f, i), sep=',')
                    self.ax.plot(self.df['E_V'], self.df['dCap_mAh_dE_V'])
        # plt.show()
        # return self.df
    
    def plotDqDvFilter(self):
        self.ncycl = [6, 21]
        self.color = cm.jet(np.linspace(0, 1, len(self.ncycl)))
        self.fig, self.ax = plt.subplots(dpi=100) 
        for n,j in enumerate(self.ncycl):
            for i in os.listdir(self.f):
                if (f"cycle_{j}.csv") in i:
                    self.df = pd.read_csv(os.path.join(self.f, i), sep=',')
                    self.ax.plot(self.df['E_V'], self.df['dCap_mAh_dE_V'], color=self.color[n])
        # plt.show()