from flask import Flask, request, render_template, redirect, flash, jsonify, session
from flask_debugtoolbar import DebugToolbarExtension
from random import randint, choice, sample

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['TESTING'] = tRUE
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

debug = DebugToolbarExtension(app)

MOVIES = {'Amadeus', 'Chicken Run', 'Dances With Wolves'}


@app.route('/')
def home_page():
    session['count'] = session.get('count', 0) + 1
    return render_template('home.html')


@app.route('/fav-color', methods=['POST'])
def fav_color():
    """show fav color"""
    fav_color = request.form.get('color')

    return render_template('color.html', fav_color=fav_color)


@app.route('/redirect-me')
def redirect_me():
    """redirect user to homepage
        302 response first
    """
    return redirect("/")


@app.route('/old-home-page')
def redirect_to_home():
    """redirect to new homepage"""
    flash('That page has moved! This is our new home page!')
    return redirect("/")


@app.route('/hello')
def say_hello():
    """return hello in html"""
    return render_template('hello.html')


@app.route('/goodbye')
def say_goodbye():
    return "GOOD BYE!!!"


@app.route('/search')
def search():
    term = request.args["term"]
    sort = request.args["sort"]

    return f"<h1>Search Results for: {term}</h> <p>Sorting by: {sort}</p>"


@app.route("/post", methods=["POST"])
def post_demo():
    return "YOU MADE A POST REQUEST!"


@app.route('/add-comment')
def add_comment_form():
    return """
    <h1>Add Comment</h1>
    <form method="POST">
        <input type="text" placeholder='comment' name='comment'/>
        <input type="text" placeholder='username' name='username'/>
        <button>Submit</button>
    </form>
    """


@app.route('/add-comment', methods=["POST"])
def save_comment():
    comment = request.form['comment']
    username = request.form['username']
    print(request.form)
    return f"""
    <h1>SAVED YOUR COMMENT</h1>
    <ul>
        <li>Userame: {username}</li>
        <li>Comment: {comment}</li>
    """


@app.route('/r/<subreddit>')
def show_subreddit(subreddit):
    return f"<h1>Browsing the {subreddit} Subreddit</h1>"


@app.route('/r/<subreddit>/comments/<int:post_id>')
def show_comments(subreddit, post_id):
    return f"<h1>Viewing comments for post with id: {post_id} from the {subreddit} Subreddit</h1>"


POSTS = {
    1: "I like chicken tenders",
    2: "I hate mayo!",
    3: "Double rainbow all the way",
    4: "YOLO OMG (kill me)"
}


@app.route('/posts/<int:id>')
def find_post(id):
    post = POSTS.get(id, "Post not found")
    return f'<p>{post}</p>'


@app.route('/lucky')
def show_lucky_num():
    """example of simple dynamic template"""

    num = randint(1, 10)

    return render_template("lucky.html", lucky_num=num, msg="You are so lucky!")


@app.route('/form')
def show_form():
    return render_template("form.html")


COMPLIMENTS = ["cool", "clever", "tenacious", "awesome", "Pythonic"]


@app.route('/greet')
def get_greeting():
    username = request.args['username']
    nice_thing = choice(COMPLIMENTS)
    return render_template("greet.html", username=username, compliment=nice_thing)


@app.route('/form-2')
def show_form_2():
    return render_template("form_2.html")


@app.route('/greet-2')
def get_greeting_2():
    username = request.args['username']
    wants = request.args.get('wants_compliments')
    nice_things = sample(COMPLIMENTS, 3)
    return render_template('greet_2.html', username=username, wants_compliments=wants, compliments=nice_things)


@app.route('/spell/<word>')
def spell_word(word):
    return render_template('spell_word.html', word=word)


@app.route('/movies')
def show_all_movies():
    """show list of all movies in fake db"""
    return render_template('movies.html', movies=MOVIES)


@app.route('/movies/new', methods=["POST"])
def add_movie():
    title = request.form['title']
    # add to pretend Db
    if title in MOVIES:
        flash('Movie Already Exists!', 'error')
    else:
        MOVIES.add(title)
        flash("Created Your Movie!", 'success')
    return redirect('/movies')


@app.route('/movies/json')
def get_movies_json():
    return jsonify(list(MOVIES))
