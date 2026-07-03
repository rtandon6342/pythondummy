from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
  return "HEllo THis is dummy web app for github actions testing"

if __name__ == "__main__":
    app.run()