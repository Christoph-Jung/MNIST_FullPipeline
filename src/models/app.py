from fastapi import FastAPI, Response
import uvicorn

import src.models.svm as svm


# class model_interface:
#     def __init__(self) -> None:
#         self.model = svm.MnistSvm()
#         self.model.load_model("test_svm.pkl")

#     def print_stuff(self) -> str:
#         return self.model.print_stuff()


app = FastAPI()
MODEL = svm.MnistSvm()
MODEL.load_model("test_svm.pkl")


@app.get("/models/svm")
def svm_root() -> Response:
    return Response("The Support Vector Machine model is running")


@app.get("/models/test")
def svm_print() -> Response:
    if MODEL is None:
        return Response("MODEL is not set")
    else:
        return Response(MODEL.print_stuff())


@app.get("/models/svm/path/{path}")
def svm_path(path: str) -> Response:
    if MODEL is None:
        return Response("MODEL is not set")
    else:
        response = MODEL.predict(path)
        return Response(f"Model prediction: {response}")


def main():
    config = uvicorn.Config("src.models.app:app", port=5000, log_level="info", reload=True, reload_dirs="src/models/")
    server = uvicorn.Server(config)
    server.run()


if __name__ == '__main__':
    main()
