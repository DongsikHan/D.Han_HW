# -*- coding: utf-8 -*-

from flask import render_template, request, flash, redirect, url_for
from apps import app, db
from models import Article, Comment
from sqlalchemy import desc

from flask.ext.wtf import Form

from wtforms import (
	StringField,
	PasswordField,
	TextAreaField
)

from wtforms import validators
from wtforms.fields.html5 import EmailField


class ArticleForm(Form):
	title = StringField(
		u'제목',
		[validators.data_required(u'제목을 입력하시기 바랍니다.')],
		description={'placeholder': u'제목을 입력하세요.'}
	)
	content = TextAreaField(
		u'내용',
		[validators.data_required(u'내용을 입력하시기 바랍니다.')],
		description={'placeholder': u'내용을 입력하세요.'}
	)
	author = StringField(
		u'작성자',
		[validators.data_required(u'이름을 입력하시기 바랍니다.')],
		description={'placeholder': u'이름을 입력하세요.'}
	)	
	category = StringField(
		u'카테고리',
		[validators.data_required(u'카테고리 입력하시기 바랍니다.')],
		description={'placeholder': u'카테고리를 입력하세요.'}
	)

class CommentForm(Form):
	author = StringField(
		u'작성자',
		[validators.data_required(u'이름을 입력하시기 바랍니다.')],
		description={'placeholder': u'이름을 입력하세요.'}
	)	
	mail = EmailField(
		u'E-mail',
		[validators.data_required(u'메일주소를 입력하시기 바랍니다.')],
		description={'placeholder': u'메일주소 입력하세요.'}
	)
	content = TextAreaField(
		u'내용',
		[validators.data_required(u'내용을 입력하시기 바랍니다.')],
		description={'placeholder': u'내용을 입력하세요.'}
	)
	password = StringField(
		u'비밀번호',
		[validators.data_required(u'비밀번호를 입력하시기 바랍니다.')],
		description={'placeholder': u'비밀번를 입력하세요.'}
	)


