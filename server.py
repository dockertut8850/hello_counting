#!/bin/python
from flask import Flask, render_template
import redis

app = Flask(__name__)

HELLO_MESSAGE = "hello, I’ve been called {0} times!"

r = redis.StrictRedis(host="redis")

@app.route("/")
def helloworld():
   return render_template("index.html",
                          message=HELLO_MESSAGE.format(r.incr("counter")))


if __name__ == "__main__":
   app.run(host="0.0.0.0", port=5000)
