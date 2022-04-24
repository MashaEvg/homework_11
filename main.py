from flask import Flask, render_template
from utils import load_candidates_from_json, get_candidates, get_candidates_by_name, get_candidates_by_skill

app = Flask(__name__)

data = load_candidates_from_json('candidates.json')


@app.route("/")
def index():
    return render_template('index.html', candidates=data)


@app.route("/candidate/<int:uid>")
def profile(uid):
    candidate = get_candidates(uid)
    return render_template('profile.html', candidate=candidate)


app.run(debug=True)
