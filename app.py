import os
from flask import *
import pymysql
pymysql.install_as_MySQLdb()
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
try:
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
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



    @app.route("/contact")
    def contact():
        return render_template('contact.html')

    @app.route("/oncontact", methods = ['GET', 'POST'])
    def oncontact():
        if(request.method=='POST'):
            entry = demo(name= request.form.get('name'), phone = request.form.get('email'), message = request.form.get('phone'),email = request.form.get('message'))
            db.session.add(entry)
            db.session.commit()
        return render_template('contact.html')

    @app.route("/post")
    def post():
        return render_template('post.html')

    if __name__ == '__main__':  
       app.run(host='0.0.0.0',debug = True)
except:
    pass
