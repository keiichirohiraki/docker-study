from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=False, nullable=False)


@app.route('/')
def hello():
    users = User.query.all()
    return render_template('hello.html', title='Hello Page', users=users)


@app.route('/user', methods=['POST'])
def register_user():
    user_name = request.form.get('user')
    db.session.add(User(name=user_name))
    db.session.commit()
    users = User.query.all()
    return render_template('hello.html', title='Hello Page', users=users)


if __name__ == '__main__':
    # DB初期化
    db.create_all()
    admin = User(name='admin')
    db.session.add(admin)
    db.session.commit()

    app.run(host='0.0.0.0', port=5000)
