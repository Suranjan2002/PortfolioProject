from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://lkrigVe1qr:BB0pvHmkF0@remotemysql.com/lkrigVe1qr'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class contact(db.Model):
    name = db.Column(db.String(200), nullable=True)
    email = db.Column(db.String(500), primary_key=True)
    message = db.Column(db.String(2500), nullable=True)
    time = db.Column(db.DateTime, default=datetime.now())

@app.route('/', methods=['GET','POST'])
def index():
    if request.method=="POST":
        name1 = request.form['name']
        email1 = request.form['email']
        message1 = request.form['message']
        date_time1 = datetime.now()

        info = contact(
            name = name1,
            email = email1,
            message = message1,
            time = date_time1
        )
        db.session.add(info)
        db.session.commit()
        
        return render_template('thankyou.html')

    info1 = contact.query.all()
    return render_template('index.html', info=info1)

if __name__=='__main__':
    app.run(debug=True)