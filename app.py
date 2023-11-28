import os

from dotenv import load_dotenv
from flask import Flask, request

load_dotenv()


app = Flask(__name__)


@app.route("/")
def main():
    name = request.args.get("name")
    message = request.args.get("message")
    return f'Hello, {name}!<br>{message}'


if __name__ == "__main__":
    app.run(
        host=os.getenv("HOST"),
        port=os.getenv("PORT"),
        debug=os.getenv("DEBUG")
    )
