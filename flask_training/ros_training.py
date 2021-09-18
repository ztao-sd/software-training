from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app=Flask(__name__)

@app.route('/')
def hello():
    return render_template('ros_training.html')

if __name__=="__main__":
    app.run(debug=True)
