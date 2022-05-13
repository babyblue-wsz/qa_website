from flask import Flask,session,g
import config
from exts import db, mail
from blueprints import qa_dp, user_dp
from flask_migrate import Migrate
from models import UserModel


app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
mail.init_app(app)

migrate = Migrate(app, db)

app.register_blueprint(qa_dp)
app.register_blueprint(user_dp)

@app.before_request
def before_request():
    user_id = session.get("user_id")
    if user_id:
        try:
            user = UserModel.query.get(user_id)
            # 给g全局变量绑定一个叫做user的变量，值是user这个对象
            # 也可以简写作  g.user = user
            setattr(g,"user",user)
        except:
            g.user = None

# 有请求 -> before_request -> 视图函数 -> 视图函数返回模板 -> context_processor
@app.context_processor
def context_processor():
    if hasattr(g,"user"):
        return {"user": g.user}
    else:
        return {}

if __name__ == '__main__':
    app.run()
