#!/usr/bin/python3

from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask(__name_)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/enternew')
def new_student():
    return render_template('student.html')

@app.route('/addrec', methods = ['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            nm = request.form.get('nm')
            addr = request.form.get('add')
            city = request.form.get('city')
            pin = request.form.get('pin')

            with sql.connect('database.db') as con:
                cur = con.cursor()

                cur.execute('INSERT INTO students (name,addr,city,pin) VALUES (?,?,?,?)',(nm,addr,city,pin))

                con.commit()
            msg = 'Record successfully added.'

        except:
            con.rollback()
            msg = 'Error in insert operation.'

        finally:
            con.close()
            return render_template('result.html', msg = msg)

@app.route('/list')
def list():
    con = sql.connect('database.db')
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute('select * from students')

    rows = cur.fetchall();
    return render_template('list.html', rows=rows)

if __name__ == '__main__':
    try:
        con = sql.connect('database.db')
        print ("Opened database successfully")
    except:
        print('Problem creating or connecting to DB.')
        exit()

    try:
        con.execute('CREATE TABLE students (name TEXT, addr TEXT, city TEXT, pin TEXT')
        print ("Table created successfully")
    except:
        pass
        
    con.close()
    app.run(port=5006)
