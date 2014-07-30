# -*- coding: utf-8 -*-
# all the imports

from flask import request, redirect, url_for,\
    render_template
from apps import app
from database import Database
from datetime import datetime

from time import gmtime, strftime


dataStorage = Database()


@app.route('/', methods=['GET', 'POST'])
def show_entries():
    entries = dataStorage.out()
    return render_template('show_entries.html', entries=entries)


@app.route('/add', methods=['POST'])
def add_entry():
    storage = {}
    storage['title'] = request.form['title']
    storage['contents'] = request.form['contents']
    storage['time'] = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    dataStorage.put(storage)
    return redirect(url_for('show_entries'))
