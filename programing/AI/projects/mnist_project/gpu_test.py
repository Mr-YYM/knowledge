import tensorflow as tf
import time

# 创建大型张量测试
size = 10000
a = tf.random.normal([size, size])
b = tf.random.normal([size, size])

start = time.time()
# 计算 a 和 b 的矩阵乘法
c = tf.matmul(a, b) 
print(f"计算耗时: {time.time()-start:.2f}秒") 
