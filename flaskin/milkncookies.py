#!/usr/bin/python

from flask import Flask, make_response, request, render_template

app = Flask(__name__)

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        user = request.form.get('nm')
        resp = make_response(render_template('readcookie.html'))
        resp.set_cookie('userID', user)
        return resp
    
    elif request.method == 'GET':
        return render_template('index.html')

@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('userID')
    if name == '':
        return 'First time to the VCP? Please login properly!'
    else:
        return f'Welcome back, {name.title()}!'


if __name__ == '__main__':
    app.run(port=5006)
