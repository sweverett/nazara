import numpy as np
from pathlib import Path
from abc import ABC, abstractmethod

class Survey(ABC):
    '''
    This is an abstract class for any survey you wish to inject into. It holds any methods that are common or need to be defined for any survey
    '''

    def __init__(self, name: str, mask: np.ndarray=None, mask_file: Path=None) -> None:
        '''
        name: str
            Name of the survey
        mask: np.ndarray
            Mask of the survey
        mask_file: str
            File path to the mask of the survey
        '''
        self.name = name
        return

    @abstractmethod
    def method1(self) -> None:
        pass