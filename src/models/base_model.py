import numpy as np
from abc import ABC, abstractmethod

from src import get_data


class BaseModel(ABC):
    def __init__(self, path: str = "") -> None:
        (train_X, train_y), (test_X, test_y) = get_data.get_mnist()
        self.train_X = train_X
        self.train_y = train_y
        self.test_X = test_X
        self.test_y = test_y
        if path != "":
            self.load_model(path)

    @abstractmethod
    def preprocess(self):
        pass

    @abstractmethod
    def create_model(self):
        pass

    @abstractmethod
    def evaluate(self):
        pass

    @abstractmethod
    def predict(self, test_data: np.ndarray):
        pass

    @abstractmethod
    def save_model(self, path: str) -> None:
        pass

    @abstractmethod
    def load_model(self, path: str) -> None:
        pass
