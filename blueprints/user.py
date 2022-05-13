import string
import random
from flask import (Blueprint, render_template, request, redirect,
                   url_for, jsonify, session, flash)
from exts import mail, db
from flask_mail import Message
from models import EmailCaptchaModel, UserModel
from datetime import datetime
from .forms import RegisterForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash

bp = Blueprint("user", __name__, url_prefix="/user")


# 登录
@bp.route("/login", methods=['POST','GET'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            user = UserModel.query.filter_by(email=email).first()
            if user and check_password_hash(user.password, password):
                session['user_id'] = user.id
                print("成功登录")
                return redirect("/")
            else:
                flash("密码验证失败")
                return redirect(url_for("user.login"))
        else:
            flash("邮箱、密码格式验证失败")
            return redirect(url_for("user.login"))

@bp.route('/logout')
def logout():
    # 清除session中所有的数据
    session.clear()
    return redirect(url_for("user.login"))

# 注册
@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        print("这是GET请求")
        return render_template("register.html")
    else:
        print("这是POST请求")
        form = RegisterForm(request.form)
        if form.validate():
            email = form.email.data
            username = form.username.data
            password = form.password.data
            # 对密码进行加密
            hash_password = generate_password_hash(password)

            user = UserModel(email=email, username=username, password=hash_password)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("user.login"))
        else:
            print("注册有问题")
            return redirect(url_for("user.register"))


# 验证码
@bp.route('/captcha', methods=['POST'])
def get_captcha():
    # 通过GET POST请求获取邮箱地址
    email = request.form.get("email")
    # 生成验证码，随机取4位
    letters = string.ascii_letters + string.digits
    captcha = "".join(random.sample(letters, 4))
    if email:
        message = Message(
            subject="flask邮箱测试",
            recipients=[email],
            body=f"这是你的验证码：{captcha}，请妥善保管哦"
        )
        mail.send(message)
        captcha_model = EmailCaptchaModel.query.filter_by(email=email).first()
        if captcha_model:
            captcha_model.captcha = captcha
            captcha_model.create_time = datetime.now()
            db.session.commit()
        else:
            captcha_model = EmailCaptchaModel(email=email, captcha=captcha)
            db.session.add(captcha_model)
            db.session.commit()
        print(captcha)
        # 200 成功请求状态码
        return jsonify({"code": 200})
    else:
        # 400 客户端错误
        return jsonify({"code": 400, "message": "请先传递邮箱！"})

# 点击网页右上角的已登录用户id，跳转至用户个人中心
@bp.route('/private')
def show_private():
    return render_template("private.html")