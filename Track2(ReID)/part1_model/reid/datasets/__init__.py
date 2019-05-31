from __future__ import absolute_import
import warnings

from .small_vehicle import Small_Vehicle
from .vehicle_downsample import Downsample_Vehicle
from .aicity_car196 import Aicity_Car196
from .aicity_attribute import Aicity_Attribute
from .complete_aicity_car196 import Complete_Aicity_Car196


__factory = {
    'small_vehicle': Small_Vehicle,
    'downsample_vehicle': Downsample_Vehicle,
    'aicity_car196': Aicity_Car196,
    'aicity_attribute': Aicity_Attribute,
    'complete_aicity_car196': Complete_Aicity_Car196,
}


def names():
    return sorted(__factory.keys())


def create(name, root, *args, **kwargs):
    """
    Create a dataset instance.

    Parameters
    ----------
    name : str
        The dataset name. Can be one of 'viper', 'cuhk01', 'cuhk03',
        'market1501', and 'dukemtmc'.
    root : str
        The path to the dataset directory.
    split_id : int, optional
        The index of data split. Default: 0
    num_val : int or float, optional
        When int, it means the number of validation identities. When float,
        it means the proportion of validation to all the trainval. Default: 100
    download : bool, optional
        If True, will download the dataset. Default: False
    """
    if name not in __factory:
        raise KeyError("Unknown dataset:", name)
    return __factory[name](root, *args, **kwargs)


def get_dataset(name, root, *args, **kwargs):
    warnings.warn("get_dataset is deprecated. Use create instead.")
    return create(name, root, *args, **kwargs)
