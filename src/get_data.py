import numpy as np
from keras.datasets import mnist


def get_mnist() -> tuple[tuple[np.ndarray, np.ndarray], tuple[np.ndarray, np.ndarray]]:
    '''
    Returns (train_X, train_y), (test_X, test_y) for the MNIST dataset
    '''
    return mnist.load_data()
