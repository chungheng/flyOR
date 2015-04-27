import numpy as np
import pandas as pd

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

if __name__ == "__main__":
    B = BaseORMap(5)
    print B[3.]
    print B(4.)
