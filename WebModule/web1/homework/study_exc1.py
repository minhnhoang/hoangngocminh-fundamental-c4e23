from flask import Flask, redirect
app = Flask(__name__)

@app.route("/about-me")
def about_me():
    return "Name: Minh Hoang, Industry: Logistics"

@app.route("/school")
def school():
    return redirect("http://techkids.vn ")

if __name__ == "__main__":
    app.run(debug=True)
