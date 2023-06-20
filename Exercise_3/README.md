# 📖 Exercise_3
主要参考: <https://github.com/open-mmlab/mmdetection/blob/tutorials/demo/MMDet_Tutorial.ipynb>

## 📁 1.文件结构

```bash
.
└── Exercise_3 # 基于 RTMDet 的气球检测
    ├── Exercise_3.ipynb # 主要脚本
    ├── rtmdet_cat_tutorial.ipynb # 上课时老师的脚本
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

<img src="output/test_balloon.jpeg" width="50%">

特征可视化结果：

<img src="../image/test_balloonAM.jpeg" width="50%">

---
# 🏷️ 任务介绍

原链接位于：[【AI实战营第二期】第三次作业提交12班 #126](https://github.com/open-mmlab/OpenMMLabCamp/issues/126)

**题目**：基于 RTMDet 的气球检测

**背景**：熟悉目标检测和 MMDetection 常用自定义流程。

**任务**
1. 基于提供的 notebook，将 cat 数据集换成气球数据集
2. 按照视频中 notebook 步骤，可视化数据集和标签
3. 使用MMDetection算法库，训练 RTMDet 气球目标检测算法，可以适当调参，提交测试集评估指标
4. 用网上下载的任意包括气球的图片进行预测，将预测结果发到群里
5. 按照视频中 notebook 步骤，对 demo 图片进行特征图可视化和 Box AM 可视化，将结果发到群里
 

**数据集**
+ 气球数据集可以直接下载 https://download.openmmlab.com/mmyolo/data/balloon_dataset.zip
+ 10 类的饮料数据集
https://github.com/TommyZihao/Train_Custom_Dataset/tree/main/%E7%9B%AE%E6%A0%87%E6%A3%80%E6%B5%8B/%E7%9B%AE%E6%A0%87%E6%A3%80%E6%B5%8B%E6%95%B0%E6%8D%AE%E9%9B%86