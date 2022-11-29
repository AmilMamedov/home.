from flask import Flask, render_template
import utils
import visualizer

app = Flask(__name__)


@app.route('/')
def page_all_candidates():
    candidates = utils.candidates_get_all()
    html_code = visualizer.build_html_some_candidates(candidates)
    return html_code


@app.route('/skills/<skill>')
def page_candidates_by_skill(skills):
    candidates = utils.candidates_get_by_skill()
    html_code = visualizer.build_html_some_candidates(candidates)
    return html_code



@app.route('/candidates/<int:pk>')
def page_candidate_by_pk(pk):
    candidate = utils.candidates_get_by_pk(pk)
    html_code = visualizer.build_html_for_one_candidate(candidate)
    return

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)