import os
from baseormap import BaseORMap

filename = os.path.join(os.path.dirname(__file__), '../data/Hallem_2006.csv')

class HallemORMap(BaseORMap):
    """
    Hallem and Carlson Dataset
    """
    def __init__(self,filename=filename):
        self._ordict = {}
        with open(filename) as f:
            self.gl = f.readline().split('\t')[1:]
            self.osn = f.readline().split('\t')[1:]
            for line in f:
                seg = line.split('\t')
                self._ordict[seg[0]] = np.array([float(x) for x in seg[1:]])
        super(HallemORMap,self).__init__(len(self._ordict))

    def __getitem__(self,item):
        c = item[0]
        return (1.-c)*self._ordict['spontaneous firing rate'] + \
               c*self._ordict[item[1]]


