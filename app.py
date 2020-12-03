from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import all_stories

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.route('/')
def choose_story():
    """ receives users choice of story """
    # print(all_stories)
    return render_template("chooseStory.html",
        storiesList = all_stories)

@app.route("/form")
def show_inputs():
    """ shows input form from story instance prompts"""
    id_selected = request.args["stories"]
    return render_template("questions.html", 
        prompts = all_stories[id_selected].prompts,
        id = id_selected)

@app.route('/<id>/results')
def show_results(id):
    """ generate story from form results and show story on page """
    story_text = all_stories[id].generate(request.args)
    return render_template("story.html", 
        story = story_text)