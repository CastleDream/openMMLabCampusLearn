
# 把一些常用的配置参数放在前面，下面去引用这些常量即可，修改会比较方便
_base_='/content/mmdetection/configs/rtmdet/rtmdet-ins_tiny_8xb32-300e_coco.py'

train_batch_size_per_gpu=32
train_num_workers=2

val_batch_size_per_gpu=4
val_num_workers=2

num_classes=1

# 由于数据集小，同时训练epoch次数少，可以把backbone固定，RTMDet的backbone就4个stage，所以下面frozen_stage=4就是全部固定（不是从0开始，就是1 2 3 4），可以看看上面的图或者论文
# 只让模型去学head部分，做下游任务的适配即可
model =dict(
  backbone = dict(frozen_stages=4),
  bbox_head=dict(dict(num_classes=num_classes))
)

# 学习率随着batchsize改变,0.04是8卡x32（每个卡的batchsize=32）的学习率,
# 12是这里设置的train_batch_size_per_gpu，
# 所以学习率要根据卡数和batchsize数（也就是计算梯度loss时实际使用的数据量）
# 0.04/(32*8)就是纯纯训练一个数据的学习率
base_lr = train_batch_size_per_gpu*0.04/(32*8)

# RTMDet训练过程分为两个Stage，第二个过程会切换数据增强pipeline，第二阶段的epoch次数是5
# max_epochs=40，也就是前35个是一套数据增强，最后5个是一套数据增强，两阶段
max_epochs=40
num_epochs_stage2=5

# 这个预训练模型组织方式和mmpretrain不一样，需要在github对应网络的readme里找，
# https://github.com/open-mmlab/mmdetection/tree/main/configs/rtmdet
# finetune 用之前训练好的预训练权重
load_from = 'https://download.openmmlab.com/mmdetection/v3.0/rtmdet/rtmdet-ins_tiny_8xb32-300e_coco/rtmdet-ins_tiny_8xb32-300e_coco_20221130_151727-ec670f7e.pth'

# 数据集改变了，则train_loader那些也要变
data_root = '/content/cat_dataset'

# metainfo这个字段在mmdetection2.0没有，3.0里才有，而且只包含两个字段，
# classes就是类别，palette就是对这个类进行可视化的时候用的颜色，也是为了方便调节吧，所以抽出来了
# 注意：classes是一个tuple，所以即使只有一个类，也应该写成`cat,`
metainfo={
  'classes':('cat',),
  'palette':[(220,20,60),]
}

train_dataloader = dict(
    batch_size=train_batch_size_per_gpu,
    num_workers=train_num_workers,
    pin_memory=True,
    dataset=dict(
        data_root=data_root,
        metainfo=metainfo,
        data_prefix=dict(img='images/'),
        ann_file='annotations/trainval.json'
    )
)

val_dataloader = dict(
    batch_size=val_batch_size_per_gpu,
    num_workers=val_num_workers,
    dataset=dict(
        data_root=data_root,
        metainfo=metainfo,
        data_prefix=dict(img='images/'),
        ann_file='annotations/test.json'
   )
)

test_dataloader = val_dataloader

# 默认的学习率调度器是warmup 1000，但是cat数据集太小了，需要修改为30 iter
param_scheduler = [
    dict(
        type='LinearLR',
        start_factor=1.0e-5,
        by_epoch=False,
        begin=0,
        end=30),
    dict(
        # use cosine lr from 10 to 20 epoch
        type='CosineAnnealingLR',
        eta_min=base_lr * 0.05,
        begin=max_epochs // 2,  #max_epoch也需要改变
        end=max_epochs,
        T_max=max_epochs // 2,
        by_epoch=True,
        convert_to_iter_based=True),
]
optim_wrapper = dict(optimizer=dict(lr=base_lr))

# 第二stage切换pipeline的epoch也变了
_base_.custom_hooks[1].switch_epoch = max_epochs-num_epochs_stage2

val_evaluator = dict(ann_file=data_root + '/annotations/test.json')
test_evaluator=val_evaluator

# 打印设置
default_hooks = dict(
    checkpoint=dict(interval=10,max_keep_ckpts=2, save_best='auto'),
    logger=dict(type='LoggerHook', interval=5))
train_cfg= dict(max_epochs=max_epochs, val_interval=10)

