import numpy as np

inputs = np.array([[0, 1, 0],
                   [0, 1, 1],
                   [0, 0, 0],
                   [1, 0, 0],
                   [1, 1, 1],
                   [1, 0, 1]])

outputs = np.array([[0], [0], [0], [1], [1], [1]])

class NeuralNetwork:
    def __init__(self,inputs, outputs):
        self.inputs = inputs
        self.outputs = outputs

        self.weights = np.array([[.50], [.50], [.50]])
        self.error_history = []
        self.epoch_list = []
        self.hidden = []
    
    def sigmoid(self,x,deriv=False):
        if deriv:
            return x * (1-x)
        return 1 / np.exp(x)

    def feed_forward(self):
        self.hidden = self.sigmoid(np.dot(self.inputs,self.weights))

    def backpropagation(self):
        self.error = self.outputs - self.hidden
        delta = self.error * self.sigmoid(self.hidden, True)
        self.weights += np.dot(self.inputs.T,delta)

    def train(self,epochs = 500):
        for epoch in range(epochs):
            self.feed_forward()
            self.backpropagation()
            self.error_history.append(np.abs(self.error))
            self.epoch_list.append(epoch)

    def predict(self,new_input):
        prediction = self.sigmoid(new_input,self.weights)
        return prediction


NN = NeuralNetwork(inputs, outputs)
NN.train()

example = np.array([[1, 1, 0]])
example_2 = np.array([[0, 1, 1]])
                                   
print(NN.predict(example), ' - Correct: ')
print(NN.predict(example_2), ' - Correct: ')