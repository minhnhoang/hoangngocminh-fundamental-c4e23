from flask import Flask, render_template

app = Flask(__name__)

@app.route("/user/<username>")
def user(username):
    users = {
        "aang": {
            "name": "Aang",
            "specialty": "the last air bender"
        },
        "katara": {
            "name": "Katara",
            "specialty": "water bending"
        },
        "beifong": {
            "name": "Toph Beifong",
            "specialty": "earth bending"
        },
        "zuko": {
            "name": "Prince Zuko",
            "specialty": "fire bending"
        }
    }
    if username in users.keys():
        user = users[username]
        return render_template("user.html", name = user["name"], specialty = user["specialty"])
    else:
        return "User not found"
    
if __name__ == "__main__":
    app.run(debug=True)