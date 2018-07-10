# MacYihuo
Project on MAC

建立当前分支是为了学习 多标签loss函数MultiLabelMarginLoss的使用
注意点如下：
1.使用MultiLabelMarginLoss函数是，输入参数2中，-1起到截断效果，即第一个-1前的值为有效值
2.使用MultiLabelMarginLoss训练出的预测结果是无序的，因此并不适合验证码的预测（可用于文本标签标记场合）
3.在确定便签个数n的情况下，通过排序，前n个值的下标即为预测值，在n未知的情况下，如何获取预测值？？？

学习文件：
pytorch_on_mac\GeneCnn.py
pytorch_on_mac\GeneData.py
