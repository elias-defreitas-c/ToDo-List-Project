from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)

    def __str__(self):
        return f'{self.id} {self.title}'

def todo_serializer(todo):
    return {
        'id': todo.id,
        'title': todo.title
    }
@app.route('/api', methods={'GET'})
def index():
    return jsonify([*map(todo_serializer, Todo.query.all())])



if __name__ == "__main__":
    with app.app_context():
        # Create the database tables
        db.create_all()
    app.run(debug=True)
