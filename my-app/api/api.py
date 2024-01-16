from flask import Flask, jsonify, request, json
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


@app.route('/', methods={'GET'})
def root():
    return 'ABC'

@app.route('/api', methods={'GET'})
def index():
    return jsonify([*map(todo_serializer, Todo.query.all())])

@app.route('/api/create', methods={'POST'})
def create():
    request_data = json.loads(request.data)
    todo = Todo(title=request_data['title'])

    db.session.add(todo)
    db.session.commit()

    return {'201': 'todo created successfully'}
@app.route('/api/<int:id>')
def show(id):
    return jsonify([*map(todo_serializer, Todo.query.filter_by(id=id))])
@app.route('/api/<int:id>', methods={'POST'})
def delete(id):
    request_data = json.loads(request.data)
    Todo.query.filter_by(id=request_data['id']).delete()
    db.session.commit()

    return {'204': 'Deleted successfully'}

if __name__ == "__main__":
    with app.app_context():
        # Create the database tables
        db.create_all()
    app.run(debug=True)
