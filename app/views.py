from flask import render_template
from app import app

@app.route('/')

def home():
   return "<b>There has been a change</b>"

@app.route('/template')

def template():
   return render_template('home.html')

@app.route('/hora')
def hora():
  from datetime import datetime
  return f'Data/hora atual {datetime.now()}'

@app.route('/soma/<int:a>/<int:b>')
def soma(a,b):
  return f'A soma é {a+b}'

