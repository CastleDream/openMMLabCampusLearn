# 🤖 简介
这个系列是OpenMMLab实战训练营第二期的学习记录，
+ 关于这个训练营的详细介绍，可以去看看：[open-mmlab/OpenMMLabCamp](https://github.com/open-mmlab/OpenMMLabCamp)
+ 我个人的博客文字记录，位于CSDN博客专栏：[OpenMMLab-AI实战营第二期](https://blog.csdn.net/castlehe/category_12337830.html)

# 🤖 作业说明
+ 作业一的README已经移至：`Exercise_1/README.md`中
+ 作业二的README已经移至：`Exercise_2/README.md`中

# 📖 Exercise_3
主要参考: <https://github.com/open-mmlab/mmdetection/blob/tutorials/demo/MMDet_Tutorial.ipynb>

## 📁 1.文件结构

```bash
.
└── Exercise_3 # 基于 RTMDet 的气球检测
    ├── Exercise_3.ipynb # 主要脚本
    ├── annotation # 气球数据集转为coco格式
    │   ├── train_coco.json
    │   └── val_coco.json
    ├── checkpoints
    │   ├── 20230611_115039.log # 日志
    │   └── best_coco_bbox_mAP_epoch_40.pth # 最有权重
    ├── output
    │   ├── cat_result.jpg # 猫的单张推理结果
    │   └── test_balloon.jpeg # 气球的单张推理结果
    ├── rtmdet-tiny_1xb12-40e_balloon.py # 气球的配置文件
    └── rtmdet-tiny_1xb12-40e_cat.py # 猫目标检测的配置文件

# 详细的COCO数据集格式

balloon_dataset/balloon
├── train
│   ├──10464445726_6f1e3bbe6a_k.jpg
│   ...
├── train_coco.json
├── val
│   ├──14898532020_ba6199dd22_k.jpg
│   ...
└── val_coco.json
```

## 📈 2.训练指标
验证集评估指标
![img](/image/3_val.png)

测试集评估指标
![img](/image/3_test.png)

## 🎆 3.测试图像
气球单张推理结果

<img src="./Exercise_3/output/test_balloon.jpeg" width="50%">

特征可视化结果：

<img src="image/test_balloonAM.jpeg" width="50%">



