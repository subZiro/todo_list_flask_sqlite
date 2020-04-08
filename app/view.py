# -*- coding: utf-8 -*-

from flask import render_template, redirect, request, flash


from app import app, db, Todo


@app.route('/', methods=['GET', 'POST'])
def index():
    """ страница приложения """
    if request.method == 'POST':
        task_content = request.form['content']
        if task_content != '':
            try:
                new_task = Todo(content=task_content)
                db.session.add(new_task)
                db.session.commit()
                flash('New task added!', 'info')
                return redirect('/')
            except Exception as e:
                return 'Error, cant write to db', e
        else:
            flash('Error, not input task', 'error')

    # не выполненые посты (статус=0)
    tasksA = Todo.query.filter(Todo.completed == False)
    tasksA = tasksA.order_by(Todo.date_created).all()
    # выполненые посты
    tasksB = Todo.query.filter(Todo.completed == True)
    tasksB = tasksB.order_by(Todo.date_created).all()

    return render_template('index.html', tasksA=tasksA, tasksB=tasksB)


@app.route('/delete/<id>/')
def delete(id):
    """ удаление таска """
    task_to_delete = Todo.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        flash('Task deleted successfully!', 'info')
        return redirect('/')
    except Exception as e:
        return f'Error, cant delete {id} task'


@app.route('/update/<id>', methods=['POST', 'GET'])
def update(id):
    """ редактирование таска """
    task = Todo.query.get_or_404(id)
    if request.method == 'POST':
        task.content = request.form['content']  # обновление контента редактируемого поста
        try:
            db.session.commit()
            return redirect('/')
        except Exception as e:
            return 'Error, cant update task', e

    return render_template('update.html', task=task)


@app.route('/check/<id>/<flag>/')
def status(id, flag):
    """ изменение статуса """
    task = Todo.query.get_or_404(id)

    if flag == 'True':
        task.completed = True
    else:
        task.completed = False
    try:
        db.session.commit()
        flash('Task update status successfully!', 'info')
        return redirect('/')
    except Exception as e:
        return 'Error, cant update task', e
