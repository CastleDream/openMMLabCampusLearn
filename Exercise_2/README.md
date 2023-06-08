# 🏷️ 任务介绍

原链接位于：[【AI实战营第二期】第二次作业提交12班 #108](https://github.com/open-mmlab/OpenMMLabCamp/issues/108)

**题目**：基于 ResNet50 的水果分类

**背景**：使用基于卷积的深度神经网络 ResNet50 对 30 种水果进行分类

**任务**
1. 划分训练集和验证集
2. 按照 MMPreTrain CustomDataset 格式组织训练集和验证集
3. 使用 MMPreTrain 算法库，编写配置文件，正确加载预训练模型
在水果数据集上进行微调训练
4. 使用 MMPreTrain 的 ImageClassificationInferencer 接口，对网络水果图像，或自己拍摄的水果图像，使用训练好的模型进行分类
5. 需提交的验证集评估指标（不能低于 60%）
   ResNet-50
   ![img](https://user-images.githubusercontent.com/94358981/243633153-f76b4aa5-e4d6-4c02-bff9-09d974268bfa.png)

**数据集**
+ 作业数据集下载：
  + 链接：https://pan.baidu.com/s/1YgoU1M_v7ridtXB9xxbA1Q
  + 提取码：52m9

+ 课程中猫狗数据集下载地址：
  + https://download.openmmlab.com/mmclassification/dataset/cats_dogs_dataset.tar