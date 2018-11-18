from flask import Flask

app = Flask(__name__)

@app.route("/bmi/<int:weight>/<int:height>")
def bmi(weight,height):
    h = height/100
    bmi = round(weight/(h*h),1)
    if bmi < 16:
        conclusion = "Severly underweight"
    elif bmi < 18.5:
        conclusion = "Underweight"
    elif bmi < 25:
        conclusion = "Normal"
    elif bmi < 30:
        conclusion = "Overweight"
    else:
        conclusion = "Obese"
    return "bmi = " + str(bmi) + conclusion

if __name__ == "__main__":
    app.run(debug=True)