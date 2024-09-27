import numpy as np

class Perceptron:
    """
    A simple perceptron model for binary classification.
    """

    def __init__(self, learning_rate: float = 0.01, n_iters: int = 1000):
        """
        Constructor for the Perceptron model.

        Parameters
        ----------
        learning_rate: float
            The learning rate for the model.
        n_iters: int
            The number of iterations to train the model.

        Attributes
        ----------
        weights: np.ndarray
            The weights for the model.
        bias: float
            The bias for the model.
        """
        self.lr = learning_rate
        self.n_iters = n_iters
        self.weights = None
        self.bias = None

    def weighted_sum(self, x: np.ndarray) -> np.ndarray:
        """
        Calculate the weighted sum of the inputs.

        Parameters
        ----------
        x: np.ndarray
            The input data.

        Returns
        -------
        np.ndarray
            The weighted sum of the inputs.
        """
        return np.dot(x, self.weights) + self.bias

    @staticmethod
    def activation_func(x: np.ndarray) -> np.ndarray:
        """
        The activation function for the perceptron.
        The function returns 1 if the input is greater than or equal to 0, otherwise it returns 0.
        This is known as the Step function.

        Parameters
        ----------
        x: np.ndarray
            The input data.

        Returns
        -------
        np.ndarray
            The output of the activation function (0 if x < 0, 1 if x >= 0).
        """
        # return np.max(x, 0)
        return np.where(x > 0, 1, 0)

    def predict(self, x: np.ndarray) -> np.ndarray:
        """
        Make a prediction using the perceptron model.

        Parameters
        ----------
        x: np.ndarray
            The input data.

        Returns
        -------
        np.ndarray
            The model predictions.
        """
        ws = self.weighted_sum(x)
        y_predicted = self.activation_func(ws)
        return y_predicted

    def fit(self, x: np.ndarray, y: np.ndarray) -> 'Perceptron':
        """
        Train the perceptron model.
        This method updates the weights and bias of the model based on the input data.

        Parameters
        ----------
        x: np.ndarray
            The input data.
        y: np.ndarray
            The target labels.
        """
        # initialize the weights and bias to random values
        n_samples, n_features = x.shape
        self.weights = np.random.uniform(size = n_features, low = -0.5, high = 0.5)
        self.bias = np.random.uniform(low = -0.5, high = 0.5)

        # train the model n_iters times
        for _ in range(self.n_iters):
            # loop through each input and output pair
            for xi, yi in zip(x, y):
                # 1. calculate y_pred (the prediction)
                y_pred = self.predict(xi)

                # 2. update the weights and bias
                # Wi = Wi + lr * (y_true - y_pred) * xi
                self.weights = self.weights + self.lr * (yi - y_pred) * xi
        return self

if __name__ == '__main__':
    # AND example
    x = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([0, 0, 0, 1])

    perceptron = Perceptron(learning_rate=0.1, n_iters=1000)
    perceptron.fit(x, y)

    y_pred = perceptron.predict(x)

    accuracy = np.mean(y == y_pred)
    print(f"Accuracy (AND example): {accuracy*100}%")
    print(f"Weights (AND example): {perceptron.weights}")
    print(f"Bias (AND example): {perceptron.bias}")

    # XOR example
    x = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([0, 1, 1, 0])

    perceptron = Perceptron(learning_rate=0.1, n_iters=1000)
    perceptron.fit(x, y)

    y_pred = perceptron.predict(x)

    # evaluate the model
    accuracy = np.mean(y == y_pred)
    print(f"Accuracy (XOR example): {accuracy*100}%")
    print(f"Weights (XOR example): {perceptron.weights}")
    print(f"Bias (XOR example): {perceptron.bias}")
