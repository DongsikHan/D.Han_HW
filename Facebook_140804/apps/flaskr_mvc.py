# -*- coding: utf-8 -*-
# all the imports

from flask import request, redirect, url_for,\
    render_template
from apps import app
from database import Database
from datetime import datetime

from time import gmtime, strftime, localtime


dataStorage = Database()

@app.route('/', methods=['GET', 'POST'])
def show_entries():
    entries = dataStorage.out()
    max_entries = dataStorage.maxlike_3()
    return render_template('show_entries.html', entries=entries, max_entries=max_entries)

@app.route('/add', methods=['POST'])
def add_entry():
    storage = {}
    storage['id'] = dataStorage.newid()
    storage['title'] = request.form['title']
    storage['contents'] = request.form['contents']
    storage['likecount'] = 0
    storage['time'] = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    dataStorage.put(storage)
    return redirect(url_for('show_entries'))

@app.route('/edit/<key>', methods=['GET'])
def edit_entry(key):
    entry = dataStorage.select(key)
    return render_template('edit.html', entry=entry)

@app.route('/editting/<key>', methods=['GET'])
def editting_entry(key):
    storage = dataStorage.select(key)
    storage['title'] = request.args['title']
    storage['contents'] = request.args['contents']
    storage['time'] = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    dataStorage.update(key, storage)
    return redirect(url_for('show_entries'))


@app.route('/del/<key>', methods=['GET'])
def del_entry(key):
    dataStorage.delete(key)
    return redirect(url_for('show_entries'))

@app.route('/like/<key>', methods=['GET'])
def like_entry(key):
    data = dataStorage.select(key)
    data['likecount'] += 1
    dataStorage.update(key, data)

    return redirect(url_for('show_entries'))

@app.route('/dislike/<key>', methods=['GET'])
def dislike_entry(key):
    data = dataStorage.select(key)
    if data['likecount'] == 0:
        data['likecount'] = 0
    else:
        data['likecount'] -= 1
    dataStorage.update(key, data)
    return redirect(url_for('show_entries'))


