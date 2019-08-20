#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)

@app.route('/hello/')
@app.route('/')
def hello_world():
    with open("helloworld.txt", 'w') as hello:
        hello.write('You just wrote this line into helloworld.txt.')    
    return 'File created\n'

if __name__ == "__main__":
    app.run(port=5006)


