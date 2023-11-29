# import
from flask import Flask

# Create a Flask app
app = Flask(__name__)

# Define route
# Create a controller
@app.route("/")
def run():
    return "{\"message\":\"Hello World Python v1\"}"

# Driver function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)