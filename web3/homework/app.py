from flask import Flask, render_template, request
import mlab
from bike import Bike

app = Flask(__name__)

mlab.connect()

@app.route("/new_bike", methods=["GET","POST"])
def new_bike():
    if request.method == "GET":
        return render_template("add_bike.html")
    elif request.method == "POST":
        form = request.form
        model = form["model"]
        fee = form["daily_fee"]
        img = form["image"]
        y = form["year"]
        b = Bike(model=model, daily_fee=fee, image=img, year=y)
        b.save()
        return "Saved"
if (__name__) == "__main__":
    app.run(debug=True)