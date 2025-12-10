# Flaskのインポート
from flask import Flask

# インスタンス作成
app: Flask = Flask(__name__)

# ルーティング
@app.route('/')
def hello_world():
    return"<h1>Hello, World!</h1>"

if __name__ == '__main__':
    app.run(debug=True)