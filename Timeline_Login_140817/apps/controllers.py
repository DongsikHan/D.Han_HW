# -*- coding: utf-8 -*-

from flask import render_template, request, redirect, url_for, flash, g, session
from apps import app, db
from models import (
    User,
    Article,
    Comment
)
from sqlalchemy import desc
from forms import ArticleForm, CommentForm, JoinForm, LoginForm
from flask.ext.wtf import Form
from wtforms import (
    StringField,
    PasswordField,
    TextAreaField
)
from wtforms import validators
from wtforms.fields.html5 import EmailField
from werkzeug.security import generate_password_hash, check_password_hash

#
#@before request
#

@app.before_request
def befor_request():
    g.user_name = None
    if 'user_email' in session:
        g.user_name = session['user_name']
        g.user_email = session['user_email']

#
# @index & article list
#

@app.route('/', methods=['GET'])
def article_list():
    context = {}

    context['article_list'] = Article.query.order_by(desc(Article.date_created)).all()

    return render_template("home.html", context=context, active_tab='timeline')


#
# @Join controllers
#
@app.route('/join', methods=['GET', 'POST'])
def user_join():
    if request.method == 'POST':

        email = request.form['email']
        password = request.form['password']
        name = request.form['name']

        user = User(
            email=email,
            password=generate_password_hash(password),
            name= name
        )

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('index'))
    #if GET
    return render_template('join.html')

@app.route('/login', methods=['GET', 'POST'])
def log_in():
    form = LoginForm()

    if request.method == 'POST':
        if form.validate_on_submit():

            email = form.email.data
            pwd = form.password.data
            user = User.query.get(email)
            
            if user is None:
                flash(u'존재하지 않는 e-mail 입니다.', 'danger')
            elif not check_password_hash(user.password, pwd):
                flash(u'password가 일치하지 않습니다.', 'danger')
            else:
                session.permanent = True
                session['user_email'] = user.email
                session['user_name'] = user.name
                flash(u'로그인 완료.', 'success')
                return redirect(url_for('article_list'))
    # if GET
    return render_template('user/login.html', form=form, active_tab='log_in')

# @app.route('/main')
# def main():
#     return render_template('home.html')

@app.route('/logout')
def log_out():
    session.clear()
    #if GET
    return redirect(url_for('article_list'))

@app.route('/article/create/', methods=['GET', 'POST'])
def article_create():
    if g.user_name == None:
        flash(u'로그인 후 이용해주세요.', 'danger')
        return redirect(url_for('log_in'))
    else:
        form = ArticleForm()
        if request.method == 'POST':
            if form.validate_on_submit():

                article = Article(
                    title = form.title.data,
                    author = form.author.data,
                    category = form.category.data,
                    content = form.content.data,
                )

            db.session.add(article)
            db.session.commit()

            flash(u'게시글을 작성하였습니다.', 'success')
            return redirect(url_for('article_list'))

    return render_template('article/create.html', form=form, active_tab='article_create')


@app.route('/article/detail/<int:id>', methods=['GET'])
def article_detail(id):
    article = Article.query.get(id)
    comments = Comment.query.order_by(desc(Comment.date_created)).filter_by(article_id=article.id)

    return render_template('article/detail.html', article=article, comments=comments)

@app.route('/article/update/<int:id>', methods=['GET', 'POST'])
def article_update(id):
    article = Article.query.get(id)
    form = ArticleForm(request.form, obj=article)
    if request.method == 'POST':
        if form.validate_on_submit():
            form.populate_obj(article)
            db.session.commit()
        
            flash(u'게시글을 수정하였습니다.', 'success')
            return redirect(url_for('article_list'))

    return render_template('article/update.html', form=form, active_tab='article_update')

@app.route('/article/delete/<int:id>', methods=['GET', 'POST'])
def article_delete(id):
    if request.method == 'GET':
        return render_template('article/delete.html', article_id=id)
    elif request.method == 'POST':
        article_id = request.form['article_id']
        article = Article.query.get(article_id)
        db.session.delete(article)
        db.session.commit()

        flash(u'게시글을 삭제하였습니다.', 'success')
        return redirect(url_for('article_list'))

# @app.route('/article/like/<int:id>', methods=['GET', 'POST'])
# def article_like(id):
#     article = Article.query.get(id)
#     article.like += 1
    
#     form = ArticleForm(request.form, obj=article)
#     if request.method == 'POST':
#         if form.validate_on_submit():
#             form.populate_obj(article)
#             db.session.commit()
        
#             flash(u'게시글을 수정하였습니다.', 'success')
#             return redirect(url_for('article_list'))

#     return render_template('article/update.html', form=form, active_tab='article_update')




#
# @comment controllers
#
@app.route('/comment/create/<int:article_id>', methods=['GET', 'POST'])
def comment_create(article_id):
    form = CommentForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            comment = Comment(
                author=form.author.data,
                email=form.email.data,
                content=form.content.data,
                password=form.password.data,
                article_id=article_id,
            )

            db.session.add(comment)
            db.session.commit()

            flash(u'댓글을 작성하였습니다.', 'success')
            return redirect(url_for('article_detail', id=article_id))
    return render_template('comment/create.html', form=form, active_tab='comment_create')

#
# @error Handlers
#
# Handle 404 errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# Handle 500 errors
@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

app.secret_key = 'asdf'