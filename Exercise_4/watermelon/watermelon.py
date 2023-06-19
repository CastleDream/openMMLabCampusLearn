# -*- encoding: utf-8 -*-
'''
@File    :   watermelon.py
@Time    :   2023/06/18 16:10:09
@Author  :   huang shan 
@Version :   1.0
@Contact :   hs8023hfp@outlook.com
@License :   (C)Copyright 2023~
@Desc    :   None
'''

from .basesegdataset import BaseSegDataset
from mmseg.registry import DATASETS
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei', 'Songti SC', 'STFangsong']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.size'] = 8


@DATASETS.register_module()
class WatermelonDataset(BaseSegDataset):
    """Cityscapes dataset.

    The ``img_suffix`` is fixed to '_leftImg8bit.png' and ``seg_map_suffix`` is
    fixed to '_gtFine_labelTrainIds.png' for Cityscapes dataset.
    """
    METAINFO = dict(
        classes=('red', 'green', 'white',
                 'seed-black', 'seed-white', 'tabBlue'),
        # rgb format
        palette=[[214, 39, 40], [44, 160, 44], [255, 255, 255],
                 [0, 0, 0], [255, 255, 255], [31, 119, 180]])

    def __init__(self,
                 img_suffix='.jpg',
                 seg_map_suffix='.png',
                 reduce_zero_label=False,
                 **kwargs) -> None:
        super().__init__(
            img_suffix=img_suffix,
            seg_map_suffix=seg_map_suffix,
            reduce_zero_label=reduce_zero_label,
            **kwargs)
