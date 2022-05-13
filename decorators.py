from flask import g, redirect, url_for
from functools import wraps

# 装饰器
def login_required(func):
    # @wraps这个装饰器一定不能忘记
    @wraps(func)
    def wrapper(*args,**kwargs):
        if hasattr(g,'user'):
            return func(*args,**kwargs)
        else:
            return redirect(url_for('user.login'))
    return wrapper