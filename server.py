from flask import (
Flask,
render_template
  )
import os

PORT = 8080
MESSAGE = "Hello, " + "brian" + "!"
print("Message: '" + MESSAGE + "'")

app = Flask(__name__)


@app.route("/")
def root():
  print("Handling web request. Returning message.")
  result = MESSAGE.encode("utf-8")
  return render_template("main-dashboard.html")

@app.route("/dashboard")
def dashboard():
  return render_template("main-dashboard.html")

@app.route("/profile")
def profile():
  return render_template("profile.html")


if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=PORT)
