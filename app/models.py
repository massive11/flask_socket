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
    name = db.Column(db.String(32), nullable=False)

    def show(self):
        return [self.account, self.password, self.name]

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


@login_manager.user_loader
def load_user(account):
    account = Account.query.get(int(account))
    return account
