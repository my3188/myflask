from flask import Flask, request, make_response, session
from flask import render_template
print('---->> 1__name__::', __name__)
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/')
def index2(name=None):
    return "首页"

@app.route('/index')
def index(name=None):
    session['username'] = 'mayue'
    response = make_response(render_template('index.html', foo=42))
    response.headers['X-Parachutes'] = 'parachutes are cool'
    return response
    # return 'index page'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    print('---sessin:', session)
    session.pop('username', None)
    print('---sessin:', session)
    return render_template('hello.html', name=name)


if __name__ == '__main__':
    print('---->> 2__name__::', __name__)
    app.run(debug=True)


# set FLASK_APP = hello.py
# set FLASK_ENV=development
