📁 文件说明

**对应的博客记录**：
|jupyter notebook|博客链接|
|---|---|
|`1.pycocotools.ipynb`和`2.图像EXIF信息.ipynb`|[OpenMMLab-AI实战营第二期——相关1. COCO数据集格式和pycocotools使用（目标检测方向）](https://stitch.blog.csdn.net/article/details/131167203)|
|`3.PatchCollection.ipynb`|[matplotlib——2. 形状和路径（Shape and Collection）底纹（hatch）](https://stitch.blog.csdn.net/article/details/131331616)|
|`4-1.数据增强可视化Openmmlab.ipynb`|[OpenMMLab-AI实战营第二期——相关3. RGB语义分割标注图像转为Gray格式的mask](https://blog.csdn.net/Castlehe/article/details/131454699)|

**文件结构**：
```bash
.
├── 1.pycocotools.ipynb # 使用pycocotools的脚本以及coco数据集格式
├── 2.图像EXIF信息.ipynb # PIL使用EXIF和OpenCV关于EXIF的说明  
├── 3.PatchCollection.ipynb # 使用PatchCollection绘制热力图，目标检测和语义分割标签显示（box/seg+标签类别文字）
├── 4-1.数据增强可视化Openmmlab.ipynb # 目标检测和语义分割/实例分割的数据增前后结果可视化，及RGB转为语义mask图像
├── 4-2.数据增强可视化Pytorch.ipynb
├── 4-3.数据增强可视化FromScratch.ipynb
├── README.md
├── datasets
│   ├── annotations # 对应balloon的标注文件
│   ├── balloon
│   ├── balloon_dataset.zip
│   ├── cat_dataset
│   └── cat_dataset.zip
└── image # 说明图像
    └── arrow_PPT.jpg
```