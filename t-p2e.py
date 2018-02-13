#import os
#os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf
a = tf.random_normal((100, 100))
b = tf.random_normal((100, 500))
j = 1000
sess = tf.InteractiveSession()
while j>= 0:
    c = tf.matmul(a, b)
    print('hello word'+str(j))
    print(sess.run(c))
    j=j-1

#with tf.Session(config= tf.ConfigProto(log_device_placement=True)) as sess:
