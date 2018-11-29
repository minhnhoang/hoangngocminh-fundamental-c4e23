from flask import Flask, render_template, request
import mlab
from movie import Movie

app = Flask(__name__)

mlab.connect()

@app.route("/add_movie", methods=["GET", "POST"])
def add_movie():
    if request.method == "GET":
        return render_template("add_movie.html") #user request form
    elif request.method == "POST":
        form = request.form
        t = form["title"]
        img = form["image"]
        y = form["year"]
        
        m = Movie(title=t, image=img, year=y)
        m.save()
        return "Gotcha!"

if __name__ == "__main__":
    app.run(debug=True)