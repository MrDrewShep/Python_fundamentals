# https://flask.palletsprojects.com/en/1.1.x/quickstart/

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello world!"

    
my_dict = {
    1: "Drew",
    2: "Matt"
}
    
@app.route('/<assigned_number>')
def provide_user_name(assigned_number):
    return my_dict[int(assigned_number)]

if __name__ == "__main__":
    app.run()
    