import numpy as np


class NeuralNet:
    def __init__(self, input_size, output_size, hidden_layer_sizes):
        self.input_size = input_size
        self.output_size = output_size
        self.hidden_layer_sizes = hidden_layer_sizes

        self.weights = []
        self.biases = []

        # Initialize weights and biases for hidden layers
        self.weights = []
        self.biases = []
        prev_size = self.input_size
        for layer_size in self.hidden_layer_sizes:
            w = np.random.randn(prev_size, layer_size)
            b = np.random.randn(layer_size)
            self.weights.append(w)
            self.biases.append(b)
            prev_size = layer_size

        # Initialize weights and biases for output layer
        w = np.random.randn(prev_size, self.output_size)
        b = np.random.randn(self.output_size)
        self.weights.append(w)
        self.biases.append(b)

    def _sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def feed_forward(self, x):
        # Compute feed forward output given input x
        a = x
        for i in range(len(self.weights)):
            z = np.dot(a, self.weights[i]) + self.biases[i]
            a = self._sigmoid(z)
        return a
