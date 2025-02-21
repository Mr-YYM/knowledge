from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import io
from pathlib import Path

# 禁用 tf 的 输出信息，TF_CPP_MIN_LOG_LEVEL 取值为 0~3，0 为显示所有信息，3 为只显示错误信息
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# 加载预训练模型
model = load_model('mnist_cnn.h5')

def preprocess_image(image):
    """将上传的图片转换为模型输入格式"""
    # 转换为灰度图并调整尺寸
    img = image.convert('L').resize((28, 28))
    # 转换为numpy数组并归一化
    img_array = np.array(img) / 255.0
    # 调整形状为(1, 28, 28, 1)
    return img_array.reshape(1, 28, 28, 1)


all_png_files = Path().glob('*.png')
for file in all_png_files:
    image = Image.open(io.BytesIO(file.read_bytes()))
    processed_img = preprocess_image(image)
    prediction = model.predict(processed_img)
    predicted_num = int(np.argmax(prediction))
    print(f'{file.name} is {predicted_num}')
