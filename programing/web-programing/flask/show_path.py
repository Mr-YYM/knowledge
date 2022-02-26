"""
返回当前的访问路径
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return '你当前访问到的路径是: %s\n' % path
