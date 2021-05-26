from . import db, app, login_manager
from flask_login import UserMixin, AnonymousUserMixin
from flask import current_app
from datetime import datetime


# 账户表
class Account(UserMixin, AnonymousUserMixin, db.Model):
    __tablename__ = 'accounts'
    account = db.Column(
        db.String(32),
        unique=True,
        primary_key=True,
        nullable=False,
        index=True)
    password = db.Column(db.String(32), nullable=False)
    type = db.Column(db.String(16), nullable=False)

    def show(self):
        return [self.account, self.password, self.type]

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.account


class AnonymousUser(AnonymousUserMixin):
    def can(self):
        return False

    def is_admin(self):
        return False


# 普通用户表
class Student(db.Model, UserMixin, AnonymousUserMixin):
    __tablename__ = 'students'
    id = db.Column(
        db.String(32),
        unique=True,
        primary_key=True,
        nullable=False,
        index=True)
    name = db.Column(db.String(32), nullable=False)

    def show(self):
        return [self.id, self.name]


# 管理员表
class Admin(db.Model, UserMixin, AnonymousUserMixin):
    __tablename__ = 'admins'
    id = db.Column(db.String(32), primary_key=True, nullable=False, index=True)
    name = db.Column(db.String(32), nullable=False)

    def show(self):
        return [self.id, self.name]


@login_manager.user_loader
def load_user(account):
    account = Account.query.get(int(account))
    if account.type == 'user':
        return Student.query.get(int(account.account))
    elif account.type == 'admin':
        return Admin.query.get(int(account.account))
    elif account in app.config['FLASKY_ADMIN']:
        return account
