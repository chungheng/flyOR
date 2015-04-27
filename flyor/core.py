from os.path import join, dirname
import numpy as np
import pandas as pd

data = {'Hallem':'Hallem_2006.tsv',
	'DoOR':'DoOR_raw.txt'}
filename = {x:join(dirname(__file__), '../data/'+y) for x,y in data.items()}

class BaseORMap(object):
    """
    Base Olfactory Receptor Mapping Class

    Attributes:
    -----------
    n : int
        number of receptors

    Methods:
    --------

    """
    def __init__(self, n):
        self.n = n # number of receptor types

    def __call__(self,*args):
        """
        Get the responses of receptors to the odorant

        resp = BaseORMap(c [,dt [,odor]])

        Use BaseORMap() instead of BaseORMap[] to read out the response of
        recpetors to odorant if BaseORMap compute response based on its
        internal state varialbes, and these variables are time variant or have
        memory.

        Parameters:
        -----------
        c : float
            concentration of the odorant

        dt : float
            time step for updating internal states

        odor : string or a tuple of strings
            a single odor identity, or a tuple representing mixture of odorants

        Returns:
        --------
        resp : ndarray
            an 1-by-n array containing the responses of n receptors

        """
        c = args[0]
        return [c]*self.n

    def __getitem__(self,item):
        """
        Get the responses of receptors to the odorant

        resp = BaseORMap(c [,odor]])

        BaseORMap[] simply read out the response of recpetors to odorant
        without updating attributes of BaseORMap.

        Parameters:
        -----------
        c : float
            concentration of the odorant

        odor : string or a tuple of strings
            a single odor identity, or a tuple representing mixture of odorants

        Returns:
        --------
        resp : ndarray
            an 1-by-n array containing the responses of n receptors

        """
        if isinstance(item,tuple):
            c = item[0]
        else:
            c = item
        return [c]*self.n

class HallemORMap(BaseORMap):
    """
    Hallem and Carlson Dataset
    """
    def __init__(self,filename=filename['Hallem']):
        self._ordict = {}
        with open(filename,'r') as f:
            self.gl = f.readline().strip('\n').split('\t')[1:]
            self.osn = f.readline().strip('\n').split('\t')[1:]
            for line in f:
                seg = line.strip('\n').split('\t')
                self._ordict[seg[0]] = np.array([float(x) for x in seg[1:]])
        super(HallemORMap,self).__init__(len(self._ordict))

    def __getitem__(self,item):
        c = item[0]
        return (1.-c)*self._ordict['spontaneous firing rate'] + \
               c*self._ordict[item[1]]

class DoORMap(BaseORMap):
    """
    DoOR Dataset
    """
    def __init__(self,filename=filename['DoOR']):
        self.df = pd.read_csv(filename, delimiter='\t')
        super(DoORMap,self).__init__(len(self.df))

if __name__ == "__main__":
    B = BaseORMap(5)
    print B[3.]
    print B(4.)
