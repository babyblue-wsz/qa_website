from flask import (Blueprint, render_template, g, request,session,
                   redirect,url_for,flash)
from decorators import login_required
from .forms import QuestionForm
from models import QuestionModel
from exts import db


bp = Blueprint("qa", __name__, url_prefix="/")


@bp.route('/')
def login():
    questions = QuestionModel.query.order_by(db.text("-create_time")).all()
    return render_template("index.html", questions=questions)


@bp.route('/question/public', methods=['GET', 'POST'])
@login_required
def public_question():
    if request.method == 'GET':
        # 判断是否已经登录，没登录就转到登录页面
        return render_template("public_question.html")
    else:
        form = QuestionForm(request.form)
        if form.validate():
            title = form.title.data
            content = form.content.data
            question = QuestionModel(title=title, content=content, author=g.user)
            db.session.add(question)
            db.session.commit()
            return redirect('/')
        else:
            flash("标题或格式错误")
            return redirect(url_for("qa.public_question"))

