from sklearn import metrics, svm

import joblib
from src.models import base_model


class MnistSvm(base_model.BaseModel):
    def preprocess(self):
        # flatten the images
        self.train_X_flatten = self.train_X.reshape((self.train_X.shape[0], -1))
        self.test_X_flatten = self.test_X.reshape((self.test_X.shape[0], -1))

    def create_model(self):
        # Create a classifier: a support vector classifier
        self.clf = svm.SVC(verbose=1, cache_size=1000, max_iter=10000)
        # Learn the digits on the train subset
        self.clf.fit(self.train_X_flatten, self.train_y)

    def evaluate(self):
        if not hasattr(self, 'test_X_flatten'):
            self.preprocess()
        test_prediction = self.clf.predict(self.test_X_flatten)
        report = metrics.classification_report(test_prediction, self.test_y)
        return report

    def predict(self, test_data):
        # Flatten test_data
        if len(test_data.shape) == 3:
            test_data_flattened = test_data.reshape((test_data.shape[0], -1))
        elif len(test_data.shape) == 2:
            test_data_flattened = test_data.reshape((1, -1))
        else:
            raise RuntimeError("Unexpected shape of test data")
        # Predict the value of the digit on the test subset
        predicted = self.clf.predict(test_data_flattened)
        return predicted

    def save_model(self, path: str) -> None:
        joblib.dump(self.clf, path)

    def load_model(self, path: str) -> None:
        self.clf = joblib.load(path)
