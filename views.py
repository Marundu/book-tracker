from flask import request
from flask import render_template
from flask import redirect

from app import app, db
from models import Task

@app.route('/')
def tasks_list():
    tasks=Task.query.all()
    return render_template('list.html', tasks=tasks)

@app.route('/task', methods=['POST'])
def add_task():
    content=request.form['content']
    if not content:
        return 'Error'
    
    task=Task(content)
    db.session.add(task)
    db.session.commit()
    return redirect('/')

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    task=Task.query.get(task_id)
    if not task:
        return redirect('/')
    
    db.session.delete(task)
    db.session.commit()
    return redirect('/')

@app.route('/done/<int:task_id>')
def resolve_task(task_id):
    task=Task.query.get(task_id)
    
    if not task:
        return redirect('/')
    if task.done:
        task.done=False
    else:
        task.done=True
    
    db.session.commit()
    return redirect('/')
