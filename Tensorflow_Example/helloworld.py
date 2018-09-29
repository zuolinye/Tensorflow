# -*- coding: utf-8 -*-
"""helloworld.ipynb

## Helloword
"""

import tensorflow as tf

# Simple hello world using TensorFlow# Simpl
hello = tf.constant('Hello, TensorFlow!')

# Start tf session
sess = tf.Session()

# Run graph
print(sess.run(hello))

