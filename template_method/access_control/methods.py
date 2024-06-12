import functools
from . import LoginPermissionChecker, VisitorPermissionChecker
from flask import abort, session
from werkzeug.exceptions import Unauthorized
from common import *

def check_login_permission(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        if not LoginPermissionChecker().check_permission(): abort(HTTP_UNAUTHORIZED)
        return f(*args, **kwargs)
    return wrapper

def check_visitor_permission(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        if not VisitorPermissionChecker().check_permission(): abort(HTTP_UNAUTHORIZED)
        return f(*args, **kwargs)
    return wrapper