import numpy as np

""" 
    Activation 
"""


# Softmax activation function
def softmax(z):
    z -= np.max(z)
    e = np.exp(z)
    return e / np.sum(e)


def softmax_grad(softmax):
    # Reshape the 1-d softmax to 2-d so that np.dot will do the matrix multiplication
    s = softmax.reshape(-1, 1)
    d = np.diagflat(s) - np.dot(s, s.T)
    return d.diagonal().reshape(2, 1).T


def tanh(z):
    return (np.exp(z) - np.exp(-z)) / (np.exp(z) + np.exp(-z))


def tanh_der(z):
    return 1 - np.power(z, 2)


def sigmoid(Z):
    return 1 / (1 + np.exp(-Z))


def relu(Z):
    return np.maximum(0, Z)


def d_relu(x):
    x[x < 0] = 0
    x[x > 0] = 1
    return x


def d_sigmoid(Z):
    s = 1 / (1 + np.exp(-Z))
    dZ = s * (1 - s)
    return dZ


class dlnet:
    def __init__(self, x, y):
        self.X = np.array(x).T
        self.Y = np.array(y).T
        self.Yh = np.zeros((1, self.Y.shape[1]))
        self.L = 2
        self.dims = [10000, 5000, 6]
        self.param = {}
        self.ch = {}
        self.lr = 0.003
        self.sam = self.Y.shape[1]

    def nInit(self):
        np.random.seed(1)
        self.param['W1'] = np.random.randn(self.dims[1], self.dims[0]) / np.sqrt(self.dims[0])
        self.param['b1'] = np.zeros((self.dims[1], 1))
        self.param['W2'] = np.random.randn(self.dims[2], self.dims[1]) / np.sqrt(self.dims[1])
        self.param['b2'] = np.zeros((self.dims[2], 1))
        return

    def forward(self):
        """
        Прямий прохід
        """
        Z1 = self.param['W1'].dot(self.X) + self.param['b1']  # x сумарне
        A1 = relu(Z1)
        self.ch['Z1'], self.ch['A1'] = Z1, A1

        Z2 = self.param['W2'].dot(A1) + self.param['b2']
        A2 = sigmoid(Z2)
        self.ch['Z2'], self.ch['A2'] = Z2, A2
        self.Yh = A2

        return self.Yh

    def nloss(self, Yh):
        loss = (1. / self.sam) * (-np.dot(self.Y, np.log(Yh).T) - np.dot(1 - self.Y, np.log(1 - Yh).T))
        return loss

    def backward(self):
        dLoss_Yh = - (np.divide(self.Y, self.Yh) - np.divide(1 - self.Y, 1 - self.Yh))

        dLoss_Z2 = dLoss_Yh * d_sigmoid(self.ch['Z2'])
        dLoss_A1 = np.dot(self.param["W2"].T, dLoss_Z2)
        dLoss_W2 = 1. / self.ch['A1'].shape[1] * np.dot(dLoss_Z2, self.ch['A1'].T)
        dLoss_b2 = 1. / self.ch['A1'].shape[1] * np.dot(dLoss_Z2, np.ones([dLoss_Z2.shape[1], 1]))

        dLoss_Z1 = dLoss_A1 * d_relu(self.ch['Z1'])
        dLoss_A0 = np.dot(self.param["W1"].T, dLoss_Z1)
        dLoss_W1 = 1. / self.X.shape[1] * np.dot(dLoss_Z1, self.X.T)
        dLoss_b1 = 1. / self.X.shape[1] * np.dot(dLoss_Z1, np.ones([dLoss_Z1.shape[1], 1]))

        self.param["W1"] = self.param["W1"] - self.lr * dLoss_W1
        self.param["b1"] = self.param["b1"] - self.lr * dLoss_b1
        self.param["W2"] = self.param["W2"] - self.lr * dLoss_W2
        self.param["b2"] = self.param["b2"] - self.lr * dLoss_b2
        return dLoss_Yh

    def gd(self, iter=3000):
        np.random.seed(1)

        self.nInit()

        for i in range(0, iter):
            Yh = self.forward()
            dloss = self.backward()

            print("Cost after iteration %i:" % (i))
            print(Yh)
            print(dloss)
        return
