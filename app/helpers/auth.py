from flask import Flask, current_app, session
from app.models.user import User
import sys

def authenticated(session):
    
    try:
        user = session["user"]
    except:
        user = ""
    return (user != "")
    
def sess_has_perm(perm):
    try:
        user = session["user"]
    except:
        user = ""

    user = User.find_by_username(user)
    if (not user):
        return False
    else:
        return user.has_perm(perm)

def current_user():
    return session.get('user')

def current_user_is_admin():
    try:
        user = session["user"]
    except:
        user = ""
    user = User.find_by_username(user)
    #print(user.username, file=sys.stderr)
    
    if (user is not None):
        return user.is_admin()
    else:
        return False
