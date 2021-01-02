import numpy as np

feature_set = np.array([[0,1,0], [0,0,1], [1,0,0],[1,1,0],[1,1,1]])
labels = np.array([[1,0,0,1,1]])
labels = labels.reshape(5,1)

#Use the seed() method to customize the start number of the random number generator.
np.random.seed(42)
weights = np.random.rand(3,1)
bias = np.random.rand(1)
lr = 0.05

def sigmoid(x):
    return 1/(1+np.exp(-x))

def sigmoid_der(x):
    return sigmoid(x)*(1-sigmoid(x))

for epoch in range(20000):
    inputs = feature_set

    #feed forward
    XW = np.dot(feature_set, weights) + bias
    z = sigmoid(XW)

    #back prop
    loss = z - labels
    print("loss: ", loss.sum())
    #MSE=1/n∑n(predicted−observed)^2
    # calculate derivative using chain rule
    dcost_dpred = loss
    dpred_dz = sigmoid_der(z)
    z_delta = dcost_dpred * dpred_dz

    inputs = feature_set.T
    weights -= lr * np.dot(inputs, z_delta)

    for num in z_delta:
        bias -= lr * num

single_point = np.array([1,0,0])
result = sigmoid(np.dot(single_point, weights) + bias)
print("result: ", result)