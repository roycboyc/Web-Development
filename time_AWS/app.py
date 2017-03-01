# coding: utf-8

from flask import Flask
import time
import os
app = Flask(__name__)


@app.route("/")
def main():
    return str(1000*time.time())


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

