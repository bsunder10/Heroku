from flask import Flask

app = Flask('name')

@app.route('/')
def home():
    return 'hello'


if __name__ == '__main__':
    app.run()
