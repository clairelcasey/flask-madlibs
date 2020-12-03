from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.route('/')
def show_inputs():
    """ shows input form from story instance prompts"""
    return render_template("questions.html", 
        prompts = silly_story.prompts)

@app.route('/results')
def show_results():
    """ generate story from form results and show story on page """
    story_text = silly_story.generate(request.args)
    return render_template("story.html", 
        story = story_text)