from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return "Testing <b>home</b> route..."


@app.route('/users/<name>')
def user(name: str) -> str:
    return (f"The user has the name: {name}.")


@app.route('/model/')
def model():
    return render_template('index.html')


def main():
    app.run(host="0.0.0.0", port=5001, debug=True)


if __name__ == '__main__':
    main()
