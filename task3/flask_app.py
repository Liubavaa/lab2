"""
Main web module
"""
from flask import Flask, render_template, request
import map_make
import tweep


app = Flask(__name__, static_folder="templates")


@app.route("/")
def index():
    """
    First page where user inputs username
    """
    return render_template('index.html')


@app.route("/map", methods=["POST"])
def map_m():
    """
    Open page with map with user friend
    """
    friend_info = tweep.friend_info(request.form.get("user_name"))
    if friend_info is None:
        return render_template('index.html')
    return map_make.iter_places(friend_info)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8082)
