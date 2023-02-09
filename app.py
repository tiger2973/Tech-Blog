import os
from flask import *
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class demo(db.Model):
    _tablename__ = 'demo'
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    phone= db.Column(db.String(10), nullable=False)
    message = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(30), nullable=False)

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/contact", methods = ['GET', 'POST'])
def contact():
    if(request.method=='POST'):
        '''Add entry to the database'''
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        entry = demo(name=name, phone = phone, message = message,email = email )
        db.session.add(entry)
        db.session.commit()
        Demos = demo.query.all()
        for i in Demos:
            print(i.name)
    return render_template('contact.html')

@app.route("/post")
def post():
    return render_template('post.html')

if __name__ == '__main__':  
   app.run(host='0.0.0.0',debug = True)
