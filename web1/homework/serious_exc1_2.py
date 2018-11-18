from flask import Flask, render_template

app = Flask(__name__)

@app.route("/bmi/<int:weight>/<int:height>")
def bmi(weight,height):
    h = height/100
    bmi = round(weight/(h*h),1)
    if bmi < 16:
        c = "Severly underweight"
    elif bmi < 18.5:
        c = "Underweight"
    elif bmi < 25:
        c = "Normal"
    elif bmi < 30:
        c = "Overweight"
    else:
        c = "Obese"
    return render_template("bmi.html", bmi = bmi, conclusion = c )
if __name__ == "__main__":
    app.run(debug=True)