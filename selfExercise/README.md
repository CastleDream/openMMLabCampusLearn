📁 文件说明
```bash
├── README.md
├── datasets
│   ├── annotations # 对应balloon的标注文件
│   ├── balloon_dataset.zip
│   └── cat_dataset.zip
└── pycocotools.ipynb # 使用pycocotools的脚本

# 注意，运行pycocotools.ipynb时，解压数据集文件后，把annotation放到balloon里，文件结构如下：捎带把train和val文件夹里自带的标注文件删除
├── balloon
│   ├── annotation
│   │   ├── train_coco.json
│   │   └── val_coco.json
│   ├── train  [61 entries exceeds filelimit, not opening dir]
│   └── val  [13 entries exceeds filelimit, not opening dir]
├── balloon_dataset.zip
└── cat_dataset.zip
```