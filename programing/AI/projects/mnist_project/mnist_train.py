import tensorflow as tf
# tensorflow.keras 是 tensorflow 中的高级 API，对 keras 进行了封装
# keras 是一个高级神经网络 API，它能够以 TensorFlow, CNTK, 或者 Theano 作为后端运行
# keras 使得神经网络的构建和训练变得非常简单
# keras 有两种模型的构建方式，一种是序贯模型(Sequential)，另一种是函数式模型(Functional)
# Sequential 是一种线性堆叠模型，它只有一个输入和一个输出，每一层只有一个输入张量和一个输出张量
# Functional 是一种灵活的模型构建方式，它可以构建多输入多输出的模型，也可以构建有环的模型
# 两种模型的构建方式都可以使用 keras.layers 中的层来构建
# keras.layers 中包含了神经网络的各种层，如全连接层(Dense)，卷积层(Conv2D)，池化层(MaxPooling2D)等
# keras.layers 中的层可以通过调用来构建模型，也可以通过继承 Layer 类来自定义层
# keras.layers 中的层可以使用激活函数，如 relu, softmax, sigmoid 等
# keras.layers 中的层可以使用正则化，如 L1, L2 正则化
# keras.layers 中的层可以使用 Dropout 防止过拟合
from tensorflow.keras.datasets import mnist

# tensorflow.keras.models 是 keras 中的模型构建模块
# Sequential 是一种模型构建方式，它是一种线性堆叠模型，只有一个输入和一个输出
# Sequential 可以通过 add 方法来添加层
from tensorflow.keras.models import Sequential

# tensorflow.keras.layers 是 keras 中的层模块
# Conv2D 是卷积层，用于提取图像的特征
# MaxPooling2D 是池化层，用于降低特征图的维度
# Flatten 是展平层，用于将多维的输入一维化
# Dense 是全连接层，用于连接卷积层与输出层
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

# 检查是否启用了 Metal GPU
print("Metal 加速是否可用:", tf.config.list_physical_devices('GPU'))

# 1. 数据加载与预处理
(x_train, y_train), (x_test, y_test) = mnist.load_data()
# 将数据转换为浮点数，并归一化
x_train = x_train.reshape(-1, 28, 28, 1).astype('float32') / 255
# 将数据转换为浮点数，并归一化
x_test = x_test.reshape(-1, 28, 28, 1).astype('float32') / 255

# 2. 构建 CNN 模型
# Sequential 表示序贯模型
# Conv2D 表示卷积层 32 表示卷积核的数量，(3,3) 表示卷积核的大小 activation 表示激活函数(relu)  input_shape 表示输入的形状
# MaxPooling2D 表示池化层 (2,2) 表示池化核的大小 
# Flatten 表示展平层 将多维的输入一维化 用于连接卷积层与全连接层 
# Dense 表示全连接层 128 表示神经元的数量 activation 表示激活函数(relu)
# Dense 表示全连接层 10 表示神经元的数量 activation 表示激活函数(softmax)
# relu 表示修正线性单元函数 softmax 表示多分类的激活函数, softmax 函数可以将神经网络的输出转换为概率分布
model = Sequential([
    Conv2D(32, (3,3), activation='relu', input_shape=(28,28,1)),
    MaxPooling2D((2,2)),
    Conv2D(64, (3,3), activation='relu'),
    MaxPooling2D((2,2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')
])

# 3. 编译与训练
# optimizer 表示优化器
# loss 表示损失函数
# metrics 表示评估指标
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 训练模型
# epochs 表示训练的轮数
# validation_data 表示验证集
model.fit(x_train, y_train, epochs=5, validation_data=(x_test, y_test))

# 4. 保存模型
model.save('mnist_cnn.h5')
