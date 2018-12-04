import ast
from flask import Flask
from flask import request
from gwrapper import logger_interface
from gwrapper import wrapper
import json
import pdb

app = Flask(__name__)

wrapper_obj = wrapper.GWrapper(
    '''{
        "url": "https://api.github.com/repos/cake-build/example",
        "username": "MariamJamal32",
        "pwd": "Mariam1374",
        "version": 1
    }''',
    logger=logger_interface.ChildLogger()
)


@app.route('/prcommitcount', methods=['POST'])
def prcommitcount():
    req_params = request.get_json()
    res = json.dumps(wrapper_obj.get_pr_with_num_of_commits(
        req_params['count'],
        req_params['filter'],
        state=req_params.get('state')
    ))
    return res


@app.route('/prcommittext', methods=['POST'])
def prcommittext():
    req_params = request.get_json()
    response_commit_text = json.dumps(wrapper_obj.get_pr_by_commit_text(
        ast.literal_eval(req_params['search_text']),
        req_params['filter'],
        state=req_params.get('state')
    ))
    return response_commit_text


@app.route('/prfilecount', methods=['POST'])
def prfilecount():
    req_params = request.get_json()
    response_file_count = json.dumps(wrapper_obj.get_pr_with_num_of_files(
        req_params['count'],
        req_params['filter'],
        state=req_params.get('state')
    ))
    return response_file_count


@app.route('/prfilename', methods=['POST'])
def prfilename():
    req_params = request.get_json()
    response_file_name = json.dumps(wrapper_obj.get_pr_by_file_name(
        ast.literal_eval(req_params['search_text']),
        req_params['filter'],
        state=req_params.get('state')
    ))
    return response_file_name


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
