from src.models import svm


def main():
    model = svm.MnistSvm("test_svm.pkl")
    test_img = model.test_X[254]
    result = model.predict(test_img)[0]
    print(f"The model thinks this number is a: {result}")


if __name__ == "__main__":
    main()
