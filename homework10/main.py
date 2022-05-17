from flask import Flask, render_template
import utils
import visual

app = Flask(__name__)


@app.route('/')
def page_all_candidates():
    candidates = utils.all_candidates()
    html_code = visual.build_html_for_some_candidates(candidates)
    return html_code


@app.route('/candidates/<int:pk>')
def page_candidate_pk(pk):

    candidate = utils.candidates_pk(pk)
    html_code = visual.build_html_for_some_candidate(candidate)
    return html_code


@app.route('/skills/')
def page_candidate_skill(skills):
    candidates = utils.all_candidates(skills)
    html_code = visual.build_html_for_some_candidates(candidates)
    return html_code


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
