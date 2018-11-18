from flask import Flask, render_template

app = Flask(__name__)

#function binding
@app.route("/") #if user access home page, call home function
def home():
    return "Hello Flask"

@app.route("/c4e")
def c4e():
    return "Hello c4e, hihi"

@app.route("/me")
def me():
    return "Name: Minh Hoang"

@app.route("/hi/<name>")
def hi(name):
    return "Hi " + name

@app.route("/add/<x>/<y>") # or ("/add/<int:x>/<int:y")
def add(x,y):
    s = int(x)+int(y)
    return str(s)

@app.route("/posts/<int:index>")
def post(index):
    title = [
        "Food",
        "Music",
        "Travel location",
    ]
    content = [
        "Burger, Pizza, Ice-cream",
        "Rap, Pop, R&B",
        "Beach, Mountain, Safari",
    ]
    t = title[index]
    c = content[index]
    return render_template("post.html",title = t , content = c)

@app.route("/movie")
def movie():
    return render_template("movie.html", name="Deadpool", image="https://cdn1us.denofgeek.com/sites/denofgeekus/files/styles/main_wide/public/2016/01/deadpool-ryan-reynolds-petition.jpg?itok=BcgLxkHQ")

@app.route("/movies")
def movies():
    # movie_titles = [
    #     "Deadpool",
    #     "Black Widow",
    #     "Captain America",
    #     "Adam Warlock"
    # ]
    movie_list = [
        {
            "title": "Deadpool",
            "image": "https://cdn1us.denofgeek.com/sites/denofgeekus/files/styles/main_wide/public/2016/01/deadpool-ryan-reynolds-petition.jpg?itok=BcgLxkHQ",
        },
        {
            "title": "Black Widow",
            "image": "https://vignette.wikia.nocookie.net/avengers-assemble/images/d/d6/Usa_avengers_skchi_blackwidow_n_6e8100ad.png/revision/latest?cb=20170426073401"
        },
        {
            "title": "Adam Warlock",
            "image": "https://i.amz.mshcdn.com/LQlTMG3urOY5IjsAxUlDzLXwQ4A=/1200x630/2018%2F05%2F08%2Fbe%2F6ede90415e0f4ec0a809a2f6947e270f.31214.jpg"
        }
    ]
    return render_template("movies.html",movies=movie_list)



if __name__ == "__main__":
    app.run(debug=True) #debug = True: allow not having to rerun code after changing