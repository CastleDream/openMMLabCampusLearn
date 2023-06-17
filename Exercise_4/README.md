# 📖 Exercise_4
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

<img src="output/test_balloon.jpeg" width="50%">

特征可视化结果：

<img src="../image/test_balloonAM.jpeg" width="50%">

---
# 🏷️ 任务介绍

原链接位于：[【AI实战营第二期】第四次作业提交12班 #393](https://github.com/open-mmlab/OpenMMLabCamp/issues/393)

**题目**：MMSeg 语义分割

**背景**：西瓜瓤、西瓜皮、西瓜籽像素级语义分割

**任务**
1. Labelme 标注语义分割数据集（子豪兄已经帮你完成了）
2. 划分训练集和测试集（子豪兄已经帮你完成了）
3. Labelme 标注转 Mask 灰度图格式（子豪兄已经帮你完成了）
4. 使用 MMSegmentation 算法库，撰写 config 配置文件，训练 PSPNet 语义分割算法
5. 提交测试集评估指标
6. 自己拍摄西瓜图片和视频，将预测结果发到群里
7. （选做）训练 Segformer 语义分割算法，提交测试集评估指标
 

**西瓜瓤、西瓜籽数据集**
+ Labelme标注格式（没有划分训练集和测试集）：https://zihao-openmmlab.obs.cn-east-3.myhuaweicloud.com/20230130-mmseg/dataset/watermelon/Watermelon87_Semantic_Seg_Labelme.zip
+ Mask标注格式（已划分训练集和测试集）：https://zihao-openmmlab.obs.cn-east-3.myhuaweicloud.com/20230130-mmseg/dataset/watermelon/Watermelon87_Semantic_Seg_Mask.zip

<img src="https://user-images.githubusercontent.com/129837368/245073269-598d8e55-62b0-438b-87c5-15fc6df9a365.png" width="60%">

<img src="https://user-images.githubusercontent.com/129837368/245073289-6d50954b-8b87-4a47-a54a-a55a720e30ac.png" width="80%">

| 类别名称     | 类别语义      | 标注类别               | 灰度图像素值 |
| ----------- | ------------ | --------------------- | ------------ |
| /           | 背景         | /                     | 0            |
| red         | 西瓜红瓤     | 多段线（polygon）       | 1            |
| green       | 西瓜外壳     | 多段线（polygon）       | 2            |
| white       | 西瓜白皮     | 多段线（polygon）       | 3            |
| seed-black  | 西瓜黑籽     | 多段线（polygon）       | 4            |
| seed-white  | 西瓜白籽     | 多段线（polygon）       | 5            |
	




