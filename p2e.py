import tensorflow as tf
a = tf.random_normal((100, 100))
b = tf.random_normal((100, 500))
c = tf.matmul(a, b)
sess = tf.InteractiveSession()
sess.run(c)
print('hello word')
print(sess.run(c))
