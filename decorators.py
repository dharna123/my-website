from flask import session
from functools import wraps


def access_control(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        if session.get("role")!="admin":
            return "Access denied"
        return func(*args,**kwargs)
    return wrapper





