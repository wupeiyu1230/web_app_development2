from flask import render_template, request, redirect, url_for, flash, session
from app.routes import auth_bp
from app.models.user import User
import functools

# Authentication decorator
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if session.get('user_id') is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view

@auth_bp.route('/register', methods=('GET', 'POST'))
def register():
    """
    GET: 顯示註冊表單
    POST: 接收註冊表單，檢查帳號是否存在，建立新使用者
    """
    pass

@auth_bp.route('/login', methods=('GET', 'POST'))
def login():
    """
    GET: 顯示登入表單
    POST: 驗證帳號密碼，成功則將 user_id 寫入 session
    """
    pass

@auth_bp.route('/logout')
def logout():
    """
    GET: 清除 session，導回登入頁面
    """
    pass
