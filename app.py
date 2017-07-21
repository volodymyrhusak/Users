# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, session, url_for
from manager import UserManager, CourseManager

from forms import ChangeUserForm, CreateUserForm

app = Flask(__name__)

app.secret_key = 'secret'


@app.route('/users', methods=["GET"])
def users():
    if request.args.get('page'):
        page = int(request.args.get('page'))
    else:
        page = 1

    if request.args.get('limit'):
        limit = int(request.args.get('limit'))
    else:
        limit = 10
    if request.args.get('data'):
        search = '%{}%'.format(request.args.get('data'))
    else:
        search = '%%'
    userManager = UserManager()
    users = userManager.getUsers(search, page, limit)
    context = {'users': users}
    return render_template('users.html', context=context)


@app.route('/change/<id>', methods=["GET", "POST"])
def changeUser(id):
    referer = request.headers.get("Referer")
    context = {'referer': referer,
               'save': False}
    err = None
    userManager = UserManager()
    user = userManager.getUser(id)
    context['user'] = user
    if request.method == "POST":
        form = ChangeUserForm(request.form, id)
        val = form.validate()
        if val == 'save':
            form.save()
            context['save'] = True
        else:
            err = val.to_primitive()
    return render_template('change_user.html', context=context, err=err)


@app.route('/create', methods=["GET", "POST"])
def createUser():
    referer = request.headers.get("Referer")
    context = {'referer': referer,
               'save': False,
               'err': None}
    if request.method == "GET":
        return render_template('create_user.html', context=context)
    elif request.method == "POST":
        form = CreateUserForm(request.form)
        val = form.validate()
        if val == 'save':
            form.save()
            context['save'] = True
        else:
            context['err'] = val.to_primitive()
        return render_template('create_user.html', context=context)


@app.route('/delete/<id>', methods=["GET"])
def deleteUser(id):
    context = {}
    userManager = UserManager()
    userManager.deleteUser(id)
    return redirect('/users')


@app.route('/courses', methods=["GET"])
def courses():
    context = {}
    courseManager = CourseManager()
    courses = courseManager.getCourse()
    context['course'] = courses
    return render_template('create_user.html', context)


@app.route('/', methods=["GET"])
def base():
    return render_template('base.html')


if __name__ == '__main__':
    app.run(debug=True)
