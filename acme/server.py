from flask import Flask

app = Flask(__name__)

@app.route("/api/")
def api_v1():
    return "Hello, API!"

if __name__ == "__main__":
    app.run(debug=True)
