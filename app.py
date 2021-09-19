from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://myremotesqldb:password@db4free.net/myremotesqldb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class contact(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=False, nullable=False)
    email = db.Column(db.String(200), unique=False, nullable=False)
    message = db.Column(db.String(1000), unique=False, nullable=False)
    datetime = db.Column(db.DateTime, default=datetime.now())

@app.route('/', methods=['GET','POST'])
def index():
    if request.method=="POST":
        name1 = request.form['name']
        email1 = request.form['email']
        message1 = request.form['message']
        datetime1 = datetime.now()

        info = contact(
            name = name1,
            email = email1,
            message = message1,
            datetime = datetime1
        )
        db.session.add(info)
        db.session.commit()
        
        return render_template('thankyou.html')

    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True, port=2581)