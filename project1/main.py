#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2025/7/4 00:19
# @Author: ms169
import dataLoading
import transformation
import dataProcessing
import cnn
import visualization
import numpy as np
import pandas as pd
from tensorflow.keras import models


def main():
    # 1. 数据加载
    data = dataLoading.DataLoading().load_all_data()
    print("数据加载完成，数据形状:", data.shape)

    # 2. 小波变换（该过程需要很长时间，建议测试时注释掉）
    for i in range(len(data)):
        nd_data = data.iloc[i].to_numpy()
        image_name = f"images/image_{i}.png"
        transformation.cwt_to_image(nd_data, image_name)
    print("小波变换完成，图像已保存。")

    # 3. 数据集处理
    train_images, test_images, train_labels, test_labels = dataProcessing.DataProcessing().process_data()
    print("数据处理完成，训练集形状:", train_images.shape, "测试集形状:", test_images.shape)

    # 4. CNN模型训练
    model = cnn.CNNModel().build_model(input_shape=(231, 310), num_classes=4)
    train_history = model.fit(train_images, train_labels, epochs=20, batch_size=16, validation_split=0.2)
    print("模型训练完成。")
    pd.DataFrame(train_history.history).to_csv("train_history.csv", index=False)  # 保存训练历史
    model.save("cnn_model.keras")  # 保存模型

    # 5. 可视化训练过程
    train_history = pd.read_csv("train_history.csv")
    visualization.plot_training_history(train_history)

    # 6. 模型评估
    model = models.load_model("cnn_model.keras")
    for i in range(10):
        prediction = model.predict(test_images[i:i + 1])
        print(f"预测标签: {dict_status[np.argmax(prediction)]}, 实际标签: {dict_status[np.argmax(test_labels[i])]}")
    avg_test_loss, avg_test_accuracy = 0, 0
    for i in range(5):
        test_loss, test_accuracy = model.evaluate(test_images, test_labels)
        avg_test_loss += test_loss
        avg_test_accuracy += test_accuracy
    avg_test_loss /= 5
    avg_test_accuracy /= 5
    print(f"平均测试损失: {avg_test_loss}, 平均测试准确率: {avg_test_accuracy}")


if __name__ == "__main__":
    dict_status = ["缺损", "正常运行", "断齿", "齿面磨损"]
    main()
