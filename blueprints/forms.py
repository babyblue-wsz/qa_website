import wtforms
from wtforms.validators import length, email, EqualTo, ValidationError, InputRequired
from models import EmailCaptchaModel, UserModel


class RegisterForm(wtforms.Form):
    username = wtforms.StringField(validators=[length(min=3, max=20)])
    email = wtforms.StringField(validators=[email()])
    captcha = wtforms.StringField(validators=[length(min=4, max=4)])
    password = wtforms.StringField(validators=[length(min=6, max=20)])
    password_confirm = wtforms.StringField(validators=[EqualTo("password")])

    # 验证 验证码是否正确
    def validate_captcha(self, field):
        captcha = field.data
        email = self.email.data
        captcha_model = EmailCaptchaModel.query.filter_by(email=email).first()
        if not captcha_model or captcha_model.captcha.lower() != captcha.lower():
            raise wtforms.ValidationError("验证码错误！")

    # 验证 邮箱是否已经被注册
    def validate_email(self, filed):
        email = filed.data
        user_model = UserModel.query.filter_by(email=email).first()
        if user_model:
            raise ValidationError("该邮箱已经存在！")


class LoginForm(wtforms.Form):
    email = wtforms.StringField(validators=[email()])
    password = wtforms.StringField(validators=[length(min=6, max=20)])


class QuestionForm(wtforms.Form):
    title = wtforms.StringField(validators=[length(min=3, max=200)])
    content = wtforms.StringField(validators=[length(min=5)])

class AnswerForm(wtforms.Form):
    content = wtforms.StringField(validators=[length(min=1)])
