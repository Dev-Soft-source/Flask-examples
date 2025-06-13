from flask import Flask, render_template, request, redirect, url_for, session, flash    
from app import app
from app.models import Todo
from app import db

@app.route('/')
def index():
    incomplete = Todo.query.filter_by(completed=False).all()
    completed = Todo.query.filter_by(completed=True).all()
    return render_template('index.html', incomplete=incomplete, completed=completed)
    
@app.route('/add', methods=['POST'])
def add():
    todo = Todo(task=request.form['todoitem'], completed=False)
    db.session.add(todo)
    db.session.commit()
    
    return redirect(url_for('index'))
    
@app.route('/complete/<id>')
def complete(id):
    todo = Todo.query.filter_by(id=int(id)).first()
    todo.completed = True
    db.session.commit()

    return redirect(url_for('index'))