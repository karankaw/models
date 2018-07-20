import tensorflow as tf

print(tf.__version__)

tensory = tf.constant([[1,2,3,4,5],
	                  [0.1, 0.2, 0.3,0,0.8],
	                  [1,2,3,4,5],
	                  [0.1, 0.2, 0.3,0,0.8],
	                  [0.1, 0.2, 0.3,0,0.8]])

tensor0 = tf.zeros([3],dtype=tf.float64)

tensor1 = tf.ones([3],dtype=tf.float64)

multipleSingleTensor = tf.constant([[1],[2],[3],[4]],dtype=tf.int32)

shape = [3]
batch_size = [5]

output = batch_size + shape 

print(output)

tf.feature_column.numeric_column

#print(tensor)

tensor = tensor0 + tensor1

with tf.Session() as session:
	tf.initialize_all_variables()
	op,ones = session.run((tensor, tensor1))#session.run takes a set of Ops/tensor to run
	# ones = session.run(tensor1)
	mst = session.run(multipleSingleTensor)
	print(multipleSingleTensor)
	#print(tensor0, tensor1, tensor0) # Multiple things can be printed on same line
	print(op)
	print(ones)
	print(mst)

#_________________________________________________________________________

feature1 = tf.feature_column.numeric_column("sepal_width", shape=(1,),dtype=tf.float32)
print(feature1)



