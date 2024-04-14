from bottle import route, run, template
import subprocess
subprocess.Popen(["python3","tenki.py"])

@route('/')
def index():
    return "<title>こんちゃ</title><h1>OKです"

run(host='0.0.0.0', port="10000")
