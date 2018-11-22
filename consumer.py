from flask import Flask
from flask import request
from gwrapper import logger_interface
from gwrapper import wrapper
import json

app = Flask(__name__)

wrapper_obj = wrapper.GWrapper(
    '''{
        "url": "https://api.github.com/repos/cake-build/example",
        "username": "MariamJamal32",
        "pwd": "Mariam1374",
        "version": 1
    }''',
    logger_interface.ChildLogger()
)


@app.route('/prcommitcount', methods=['POST'])
def prcommitcount():
    res = json.dumps(wrapper_obj.get_pr_with_num_of_commits(
        request.get_json()['count'],
        request.get_json()['filter']
    ))
    return res


@app.route('/prcommittext', methods=['POST'])
def prcommittext():
    response_commit_text = json.dumps(wrapper_obj.get_pr_by_commit_text(
        request.get_json()['search_text'],
        request.get_json()['filter']
    ))
    return response_commit_text


@app.route('/prfilecount', methods=['POST'])
def prfilecount():
    response_file_count = json.dumps(wrapper_obj.get_pr_with_num_of_files(
        request.get_json()['count'],
        request.get_json()['filter']
    ))
    return response_file_count


@app.route('/prfilename', methods=['POST'])
def prfilename():
    response_file_name = json.dumps(wrapper_obj.get_pr_with_num_of_files(
        request.get_json()['search_text'],
        request.get_json()['filter']
    ))
    return response_file_name


if __name__ == '__main__':
    app.run(debug=True)
