# import
from flask import Flask, render_template

# Create a Flask app
app = Flask(__name__)


# Define route
# Create a controller
@app.route("/")
def run():
    return "{\"message\":\"Hello World Python v1\"}"

@app.route('/user/<name>')
def hello(name=None):
  #name=None ensures the code runs even when no name is provided
  return render_template('./user-profile.html', name=name)

# Driver function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)