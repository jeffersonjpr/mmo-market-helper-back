from flask import Flask
from app.routes.item_route import item_route
from app.routes.type_route import type_route

app = Flask(__name__)

app.register_blueprint(item_route)
app.register_blueprint(type_route)


@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(debug=True)
